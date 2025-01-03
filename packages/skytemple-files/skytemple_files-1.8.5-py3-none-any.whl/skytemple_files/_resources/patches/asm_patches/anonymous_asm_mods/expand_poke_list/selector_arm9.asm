; For use with ARMIPS
; 2021/04/14
; For Explorers of Sky All Versions
; ------------------------------------------------------------------------------
; Selects the correct version to use
; ------------------------------------------------------------------------------

.relativeinclude on

; Selects the correct region to apply the patch
.if PPMD_GameVer == GameVer_EoS_NA
	.include "na/constants.asm"
	.include "na/offsets.asm"
	.include "common/patch_arm9.asm"
.elseif PPMD_GameVer == GameVer_EoS_EU
	.include "eu/constants.asm"
	.include "eu/offsets.asm"
	.include "common/patch_arm9.asm"
.elseif PPMD_GameVer == GameVer_EoS_JP
	.include "jp/constants.asm"
	.include "jp/offsets.asm"
	.include "common/patch_arm9.asm"
.endif

.relativeinclude off
