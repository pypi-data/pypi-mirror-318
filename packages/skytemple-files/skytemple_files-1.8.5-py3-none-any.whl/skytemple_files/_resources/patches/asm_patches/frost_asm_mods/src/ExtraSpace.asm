; ----------------------------------------------------------------------
; Copyright © 2021 Frostbyte0x70
; 
; This program is free software: you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation, either version 3 of the License, or
; (at your option) any later version.
; 
; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
; 
; You should have received a copy of the GNU General Public License
; along with this program.  If not, see <https://www.gnu.org/licenses/>.
; ----------------------------------------------------------------------

; This hack loads a new overlay named overlay_0036.bin into an unused area of the RAM shortly after the game starts (right after overlay_0010.bin is loaded).
; This won't have any effect on its own, but overlay_0036.bin can be patched to insert extra data or code needed for other ASM patches.
; The overlay must be present in the ROM already, this patch won't add it.

; This file is intended to be used with armips v0.11
; Required ROM: Explorers of Sky (EU/US/JP)
; Required files: arm9.bin, y9.bin
;	In addition, overlay_0036.bin must be present in the ROM with a size of 0x38F80 bytes.

; Set to 1 to skip patching y9.bin (Useful if you want to edit the overlay list yourself)
SKIP_Y9 equ 0

.nds
.include "common/regionSelect.asm"

.open "arm9.bin", arm9
; #####################################
; ##          Optimizations          ##
; #####################################

; The overlay load function has two switches. The fisrt one has 6 cases (+ the default case), but the last 3 are duplicates.
; They can be removed to get some free space.
; We have to modify the jumps to those duplicated cases so they jump to one of the first three instead.
.org EU_20040F8
.area 0x2004158 - 0x20040F8
	b EU_2004168
	b EU_2004168
	b EU_2004168
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
	b EU_2004174
.endarea

; Now we can use this space to add extra code. We are going to take a section of the function and turn in into another smaller function since
; it's now going to be used more than once
; -----------------
; Loads an overlay in the RAM, checks if the load was successful and calls what is probably a fallback function if it's not
; sp+10h: Buffer containing a copy of the entry inside the overlay list corresponding to the overlay to load
; -----------------
.org EU_2004180
.area 0x20041A4 - 0x2004180
@loadOverlay:
	push lr
	add r0,sp,10h+4 ; We need to account for the extra register we pushed
	bl LoadOverlayInRam
	cmp r0,0h
	moveq r0,1h
	bleq LoadOverlayFallback
	add r0,sp,10h+4
	bl EU_2080254 ; Jumps to the static initializer addresses, among other things
	pop pc
.endarea

; Next, we optimize the end of the function. We can remove the code that we have turned into a separate function. Also, there are some
; constants that are loaded using an ldr instruction that can all be turned into mov instructions, saving more space.
.org EU_2004270
	mov r2,0h
.org EU_2004270 + 24h * 1
	mov r2,0Ah
.org EU_2004270 + 24h * 2
	mov r2,23h
.org EU_2004270 + 24h * 3
	mov r2,1h
.org EU_2004270 + 24h * 4
	mov r2,2h
.org EU_2004270 + 24h * 5
	mov r2,3h
.org EU_2004270 + 24h * 6
	mov r2,6h
.org EU_2004270 + 24h * 7
	mov r2,4h
.org EU_2004270 + 24h * 8
	mov r2,5h
.org EU_2004270 + 24h * 9
	mov r2,7h
.org EU_2004270 + 24h * 10
	mov r2,8h
.org EU_2004270 + 24h * 11
	mov r2,9h
.org EU_2004270 + 24h * 12
	mov r2,0Bh
.org EU_2004270 + 24h * 13
	mov r2,1Dh
.org EU_2004270 + 24h * 14
	mov r2,22h
.org EU_2004270 + 24h * 15
	mov r2,0Ch
.org EU_2004270 + 24h * 16
	mov r2,0Dh
.org EU_2004270 + 24h * 17
	mov r2,0Eh
.org EU_2004270 + 24h * 18
	mov r2,0Fh
.org EU_2004270 + 24h * 19
	mov r2,10h
.org EU_2004270 + 24h * 20
	mov r2,11h
.org EU_2004270 + 24h * 21
	mov r2,12h
.org EU_2004270 + 24h * 22
	mov r2,13h
.org EU_2004270 + 24h * 23
	mov r2,14h
.org EU_2004270 + 24h * 24
	mov r2,15h
.org EU_2004270 + 24h * 25
	mov r2,16h
.org EU_2004270 + 24h * 26
	mov r2,17h
.org EU_2004270 + 24h * 27
	mov r2,18h
.org EU_2004270 + 24h * 28
	mov r2,19h
.org EU_2004270 + 24h * 29
	mov r2,1Ah
.org EU_2004270 + 24h * 30
	mov r2,1Bh
.org EU_2004270 + 24h * 31
	mov r2,1Ch
.org EU_2004270 + 24h * 32
	mov r2,1Eh
.org EU_2004270 + 24h * 33
	mov r2,1Fh
.org EU_2004270 + 24h * 34
	mov r2,20h
.org EU_2004270 + 24h * 35
	mov r2,21h

.org EU_20047A0
	; Original code replaced with a call to the new function
	bl @loadOverlay
	; Move the end of the current function here
@endFunc:
	bl EU_2008194
@return:
	add sp,sp,3Ch
	pop r3,r4,pc
@pool:
	.word EU_20AFAD0
	.word EU_20928F0
	.word EU_2092938
	; The rest of the literals are no longer necessary
@freeSpace:

; Since we have shifted the end of the function, we have to update some offsets
.org EU_2004158
	b @return
.org EU_200415C
	ldr r0,[@pool]
.org EU_2004168
	ldr r0,[@pool]
.org EU_2004174
	ldr r0,[@pool]
.org EU_20041A4
	ldr r1,[@pool+4]
.org EU_20041B4
	ldr r1,[@pool+8]
.org EU_2004780
	ldr r1,[@pool+4]
.org EU_2004790
	ldr r1,[@pool+8]

; #####################################
; ##          Actual patch           ##
; #####################################
.org @freeSpace
.area EU_2004868 - .
@ov36AlreadyLoaded:
	.word 0 ; Set to 1 after loading our extra overlay. Has to be a word so we can directly load it with an ldr.
@loadOverlay36:
	push lr
	; Set the overlay loaded byte
	mov r0,1h
	str r0,[@ov36AlreadyLoaded]
	; Now get the data for overlay 36 and load it
	mov r2,24h
	add r0,sp,10h
	mov r1,0h
	bl GetOverlayData
	cmp r0,0h
	; If something went wrong, call the fallback function first
	moveq r0,1h
	bleq LoadOverlayFallback
	bl @loadOverlay

	; Original instruction
	mov r0, 0h

	pop pc
.endarea

; -----------------
; These hooks were used in the previous version of the patch,
; restore the original instructions
; -----------------
.org EU_20042A8
	bne EU_20047A0
.org EU_20042B4
	b EU_20047A0

; -----------------
; Hook inside `NitroMain`, which is pretty early in the game's
; initialization process
; -----------------
.org NitroMain+34h
	bl @loadOverlay36
.close

; -----------------
; Overlay list patch
; We have to add a new entry to the overlay list for overlay 36
; -----------------
.if SKIP_Y9 != 1
	.open "y9.bin", 0
	.org 0x480
		.word 24h ; Overlay ID
		.word ov_36 ; RAM load address
		.word 0x38F80 ; Overlay size (Size of the empty RAM area)
		.word 0 ; "Size of BSS data region". Zero I guess?
		; Static initializer start address. Start of an array that can be used by other projects that make use of this patch to
		; run some init code when the overlay is loaded.
		.word ov_36 + 0xC40
		; Static initializer end address. The array has 32 slots in total, which should be more than enough.
		.word ov_36 + 0xCC0
		.word 24h ; File ID
		.word 0 ; Reserved (Always 0)
	
	.close
.endif