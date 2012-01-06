sampleDataSet = '/DYToEE_M-20_TuneZ2_7TeV-pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM'
sampleCMSEnergy = 7000

sampleRelease = "CMSSW_4_2_2_patch2" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_4_2_7" # release used to create new files with

sampleNumEvents = 2262653

sampleXSec = 1300 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START42_V13::All'
sampleHLTProcess = '*'

sampleBaseDir = "root://xrootd.rcac.purdue.edu//store/user/demattia/longlived/"+sampleProcessRelease+"/Zee"

sampleRecoFiles = [ ]

samplePatFiles = [
  sampleBaseDir+"/pat/PATtuple_1_1_pll.root",
  sampleBaseDir+"/pat/PATtuple_2_1_Fwf.root",
  sampleBaseDir+"/pat/PATtuple_3_1_PFX.root",
  sampleBaseDir+"/pat/PATtuple_4_1_MCU.root",
  sampleBaseDir+"/pat/PATtuple_5_1_uli.root",
  sampleBaseDir+"/pat/PATtuple_6_1_RJz.root",
  sampleBaseDir+"/pat/PATtuple_7_1_tek.root",
  sampleBaseDir+"/pat/PATtuple_8_1_dfG.root",
  sampleBaseDir+"/pat/PATtuple_9_1_Bvq.root",
  sampleBaseDir+"/pat/PATtuple_10_1_StX.root",
  sampleBaseDir+"/pat/PATtuple_11_1_1Yx.root",
  sampleBaseDir+"/pat/PATtuple_12_1_zJg.root",
  sampleBaseDir+"/pat/PATtuple_13_1_4mY.root",
  sampleBaseDir+"/pat/PATtuple_14_1_apF.root",
  sampleBaseDir+"/pat/PATtuple_15_1_1A9.root",
  sampleBaseDir+"/pat/PATtuple_16_1_6e6.root",
  sampleBaseDir+"/pat/PATtuple_17_1_lqt.root",
  sampleBaseDir+"/pat/PATtuple_18_1_GUr.root",
  sampleBaseDir+"/pat/PATtuple_19_1_Pls.root",
  sampleBaseDir+"/pat/PATtuple_20_1_3c1.root",
  sampleBaseDir+"/pat/PATtuple_21_1_7rl.root",
  sampleBaseDir+"/pat/PATtuple_22_1_ZIo.root",
  sampleBaseDir+"/pat/PATtuple_23_1_98U.root",
  sampleBaseDir+"/pat/PATtuple_24_1_J70.root",
  sampleBaseDir+"/pat/PATtuple_25_1_31U.root",
  sampleBaseDir+"/pat/PATtuple_26_1_KyL.root",
  sampleBaseDir+"/pat/PATtuple_27_1_rLR.root",
  sampleBaseDir+"/pat/PATtuple_28_1_IVL.root",
  sampleBaseDir+"/pat/PATtuple_29_1_O05.root",
  sampleBaseDir+"/pat/PATtuple_30_1_CTX.root",
  sampleBaseDir+"/pat/PATtuple_31_1_DI8.root",
  sampleBaseDir+"/pat/PATtuple_32_1_nwg.root",
  sampleBaseDir+"/pat/PATtuple_33_1_cd4.root",
  sampleBaseDir+"/pat/PATtuple_34_1_uwx.root",
  sampleBaseDir+"/pat/PATtuple_35_1_UHO.root",
  sampleBaseDir+"/pat/PATtuple_36_1_9w9.root",
  sampleBaseDir+"/pat/PATtuple_37_1_DcJ.root",
  sampleBaseDir+"/pat/PATtuple_38_1_TL3.root",
  sampleBaseDir+"/pat/PATtuple_39_1_eBb.root",
  sampleBaseDir+"/pat/PATtuple_40_1_ngE.root",
  sampleBaseDir+"/pat/PATtuple_41_1_qwT.root",
  sampleBaseDir+"/pat/PATtuple_42_1_kih.root",
  sampleBaseDir+"/pat/PATtuple_43_1_aEQ.root",
  sampleBaseDir+"/pat/PATtuple_44_1_14k.root",
  sampleBaseDir+"/pat/PATtuple_45_1_qwD.root",
  sampleBaseDir+"/pat/PATtuple_46_1_OxI.root",
  sampleBaseDir+"/pat/PATtuple_47_1_cm2.root",
  sampleBaseDir+"/pat/PATtuple_48_1_dxk.root",
  sampleBaseDir+"/pat/PATtuple_49_1_ERk.root",
  sampleBaseDir+"/pat/PATtuple_50_1_ISq.root",
  sampleBaseDir+"/pat/PATtuple_51_0_rbO.root",
  sampleBaseDir+"/pat/PATtuple_52_0_9pA.root",
  sampleBaseDir+"/pat/PATtuple_53_0_4Sy.root",
  sampleBaseDir+"/pat/PATtuple_54_0_Pvh.root",
  sampleBaseDir+"/pat/PATtuple_55_0_JPs.root",
  sampleBaseDir+"/pat/PATtuple_56_0_tsq.root",
  sampleBaseDir+"/pat/PATtuple_57_0_CqQ.root",
  sampleBaseDir+"/pat/PATtuple_58_0_LIc.root",
  sampleBaseDir+"/pat/PATtuple_59_0_AGK.root",
  sampleBaseDir+"/pat/PATtuple_60_0_Mmj.root",
  sampleBaseDir+"/pat/PATtuple_61_0_AYl.root",
  sampleBaseDir+"/pat/PATtuple_62_0_VJ8.root",
  sampleBaseDir+"/pat/PATtuple_63_0_DZP.root",
  sampleBaseDir+"/pat/PATtuple_64_0_nhC.root",
  sampleBaseDir+"/pat/PATtuple_65_0_0sF.root",
  sampleBaseDir+"/pat/PATtuple_66_0_6Lk.root",
  sampleBaseDir+"/pat/PATtuple_67_0_o8X.root",
  sampleBaseDir+"/pat/PATtuple_68_0_Tad.root",
  sampleBaseDir+"/pat/PATtuple_69_0_cCV.root",
  sampleBaseDir+"/pat/PATtuple_70_0_Zjd.root",
  sampleBaseDir+"/pat/PATtuple_71_0_UHq.root",
  sampleBaseDir+"/pat/PATtuple_72_0_fe0.root",
  sampleBaseDir+"/pat/PATtuple_73_0_niz.root",
  sampleBaseDir+"/pat/PATtuple_74_0_U4N.root",
  sampleBaseDir+"/pat/PATtuple_75_0_W8m.root",
  sampleBaseDir+"/pat/PATtuple_76_0_hP6.root",
  sampleBaseDir+"/pat/PATtuple_77_0_FTw.root",
  sampleBaseDir+"/pat/PATtuple_78_0_mfc.root",
  sampleBaseDir+"/pat/PATtuple_79_0_0v9.root",
  sampleBaseDir+"/pat/PATtuple_80_0_dMB.root",
  sampleBaseDir+"/pat/PATtuple_81_0_fDD.root",
  sampleBaseDir+"/pat/PATtuple_82_0_FVi.root",
  sampleBaseDir+"/pat/PATtuple_83_0_C8j.root",
  sampleBaseDir+"/pat/PATtuple_84_0_SUA.root",
  sampleBaseDir+"/pat/PATtuple_85_0_y0c.root",
  sampleBaseDir+"/pat/PATtuple_86_0_eqO.root",
  sampleBaseDir+"/pat/PATtuple_87_0_fXq.root",
  sampleBaseDir+"/pat/PATtuple_88_0_Myy.root",
  sampleBaseDir+"/pat/PATtuple_89_0_5oU.root",
  sampleBaseDir+"/pat/PATtuple_90_0_srN.root",
  sampleBaseDir+"/pat/PATtuple_91_0_L0z.root",
  sampleBaseDir+"/pat/PATtuple_92_0_dj7.root",
  sampleBaseDir+"/pat/PATtuple_93_0_aW4.root",
  sampleBaseDir+"/pat/PATtuple_94_0_y2o.root",
  sampleBaseDir+"/pat/PATtuple_95_0_GpQ.root",
  sampleBaseDir+"/pat/PATtuple_96_0_fla.root",
  sampleBaseDir+"/pat/PATtuple_97_0_7FR.root",
  sampleBaseDir+"/pat/PATtuple_98_0_5qk.root",
  sampleBaseDir+"/pat/PATtuple_99_0_LUF.root",
  sampleBaseDir+"/pat/PATtuple_100_0_9wq.root",
  sampleBaseDir+"/pat/PATtuple_101_0_2D5.root",
  sampleBaseDir+"/pat/PATtuple_102_0_Y3I.root",
  sampleBaseDir+"/pat/PATtuple_103_0_NLW.root",
  sampleBaseDir+"/pat/PATtuple_104_0_4XS.root",
  sampleBaseDir+"/pat/PATtuple_105_0_RlY.root",
  sampleBaseDir+"/pat/PATtuple_106_0_D96.root",
  sampleBaseDir+"/pat/PATtuple_107_0_HAE.root",
  sampleBaseDir+"/pat/PATtuple_108_0_Y7Q.root",
  sampleBaseDir+"/pat/PATtuple_109_0_zqM.root",
  sampleBaseDir+"/pat/PATtuple_110_0_RBB.root",
  sampleBaseDir+"/pat/PATtuple_111_0_VTM.root",
  sampleBaseDir+"/pat/PATtuple_112_0_jMW.root",
  sampleBaseDir+"/pat/PATtuple_113_0_EMG.root",
  sampleBaseDir+"/pat/PATtuple_114_0_2ZN.root",
  sampleBaseDir+"/pat/PATtuple_115_0_UbB.root",
  sampleBaseDir+"/pat/PATtuple_116_0_YXq.root",
  sampleBaseDir+"/pat/PATtuple_117_0_Dvc.root",
  sampleBaseDir+"/pat/PATtuple_118_1_Ell.root",
  sampleBaseDir+"/pat/PATtuple_119_0_364.root",
  sampleBaseDir+"/pat/PATtuple_120_1_fco.root",
  sampleBaseDir+"/pat/PATtuple_121_0_yoC.root",
  sampleBaseDir+"/pat/PATtuple_122_0_vTq.root",
  sampleBaseDir+"/pat/PATtuple_123_1_JBb.root",
  sampleBaseDir+"/pat/PATtuple_124_1_YYY.root",
  sampleBaseDir+"/pat/PATtuple_125_0_2tz.root",
  sampleBaseDir+"/pat/PATtuple_126_0_AYK.root",
  sampleBaseDir+"/pat/PATtuple_127_0_7py.root",
  sampleBaseDir+"/pat/PATtuple_128_0_fCk.root",
  sampleBaseDir+"/pat/PATtuple_129_0_EaY.root",
  sampleBaseDir+"/pat/PATtuple_130_0_dWw.root",
  sampleBaseDir+"/pat/PATtuple_131_0_PWG.root",
  sampleBaseDir+"/pat/PATtuple_132_0_Efx.root",
  sampleBaseDir+"/pat/PATtuple_133_0_Idx.root",
  sampleBaseDir+"/pat/PATtuple_134_0_s0M.root",
  sampleBaseDir+"/pat/PATtuple_135_1_ak6.root",
  sampleBaseDir+"/pat/PATtuple_136_1_kvW.root",
  sampleBaseDir+"/pat/PATtuple_137_0_Xff.root",
  sampleBaseDir+"/pat/PATtuple_138_1_wlW.root",
  sampleBaseDir+"/pat/PATtuple_139_0_em7.root",
  sampleBaseDir+"/pat/PATtuple_140_0_3yV.root",
  sampleBaseDir+"/pat/PATtuple_141_0_TcQ.root",
  sampleBaseDir+"/pat/PATtuple_142_0_hDI.root",
  sampleBaseDir+"/pat/PATtuple_143_0_qON.root",
  sampleBaseDir+"/pat/PATtuple_144_0_mDb.root",
  sampleBaseDir+"/pat/PATtuple_145_0_q1T.root",
  sampleBaseDir+"/pat/PATtuple_146_0_iqI.root",
  sampleBaseDir+"/pat/PATtuple_147_0_orx.root",
  sampleBaseDir+"/pat/PATtuple_148_0_VP6.root",
  sampleBaseDir+"/pat/PATtuple_149_0_5jz.root",
  sampleBaseDir+"/pat/PATtuple_150_0_mf1.root",
  sampleBaseDir+"/pat/PATtuple_151_0_9NP.root",
  sampleBaseDir+"/pat/PATtuple_152_0_kjF.root",
  sampleBaseDir+"/pat/PATtuple_153_0_fx7.root",
  sampleBaseDir+"/pat/PATtuple_154_0_2P0.root",
  sampleBaseDir+"/pat/PATtuple_155_0_9G1.root",
  sampleBaseDir+"/pat/PATtuple_156_0_tgS.root",
  sampleBaseDir+"/pat/PATtuple_157_0_aSP.root",
  sampleBaseDir+"/pat/PATtuple_158_0_VDA.root",
  sampleBaseDir+"/pat/PATtuple_159_0_Ahs.root",
  sampleBaseDir+"/pat/PATtuple_160_0_9a7.root",
  sampleBaseDir+"/pat/PATtuple_161_0_jsg.root",
  sampleBaseDir+"/pat/PATtuple_162_0_B4P.root",
  sampleBaseDir+"/pat/PATtuple_163_0_bpS.root",
  sampleBaseDir+"/pat/PATtuple_164_0_h4V.root",
  sampleBaseDir+"/pat/PATtuple_165_0_LRE.root",
  sampleBaseDir+"/pat/PATtuple_166_0_uQJ.root",
  sampleBaseDir+"/pat/PATtuple_167_0_Jtj.root",
  sampleBaseDir+"/pat/PATtuple_168_0_Dka.root",
  sampleBaseDir+"/pat/PATtuple_169_0_whz.root",
  sampleBaseDir+"/pat/PATtuple_170_0_GEp.root",
  sampleBaseDir+"/pat/PATtuple_171_0_uWf.root",
  sampleBaseDir+"/pat/PATtuple_172_0_gQF.root",
  sampleBaseDir+"/pat/PATtuple_173_0_C1g.root",
  sampleBaseDir+"/pat/PATtuple_174_0_Dfs.root",
  sampleBaseDir+"/pat/PATtuple_175_0_Fvr.root",
  sampleBaseDir+"/pat/PATtuple_176_0_46d.root",
  sampleBaseDir+"/pat/PATtuple_177_0_Wkh.root",
  sampleBaseDir+"/pat/PATtuple_178_0_By7.root",
  sampleBaseDir+"/pat/PATtuple_179_0_uko.root",
  sampleBaseDir+"/pat/PATtuple_180_0_Wy2.root",
  sampleBaseDir+"/pat/PATtuple_181_0_Apb.root",
  sampleBaseDir+"/pat/PATtuple_182_0_ITb.root",
  sampleBaseDir+"/pat/PATtuple_183_0_lsr.root",
  sampleBaseDir+"/pat/PATtuple_184_0_Aeh.root",
  sampleBaseDir+"/pat/PATtuple_185_0_FbM.root",
  sampleBaseDir+"/pat/PATtuple_186_0_aX0.root",
  sampleBaseDir+"/pat/PATtuple_187_0_ouJ.root",
  sampleBaseDir+"/pat/PATtuple_188_0_6VF.root",
  sampleBaseDir+"/pat/PATtuple_189_0_mXx.root",
  sampleBaseDir+"/pat/PATtuple_190_0_Zve.root",
  sampleBaseDir+"/pat/PATtuple_191_0_ZCD.root",
  sampleBaseDir+"/pat/PATtuple_192_0_nOq.root",
  sampleBaseDir+"/pat/PATtuple_193_0_9lv.root",
  sampleBaseDir+"/pat/PATtuple_194_0_CBI.root",
  sampleBaseDir+"/pat/PATtuple_195_0_TGP.root",
  sampleBaseDir+"/pat/PATtuple_196_0_3Vg.root",
  sampleBaseDir+"/pat/PATtuple_197_0_cYU.root",
  sampleBaseDir+"/pat/PATtuple_198_0_aGM.root",
  sampleBaseDir+"/pat/PATtuple_199_0_dxr.root",
  sampleBaseDir+"/pat/PATtuple_200_0_2K8.root",
  sampleBaseDir+"/pat/PATtuple_201_0_h9v.root",
  sampleBaseDir+"/pat/PATtuple_202_0_EDj.root",
  sampleBaseDir+"/pat/PATtuple_203_0_7ZW.root",
  sampleBaseDir+"/pat/PATtuple_204_0_1sR.root",
  sampleBaseDir+"/pat/PATtuple_205_0_NE9.root",
  sampleBaseDir+"/pat/PATtuple_206_0_EJx.root",
  sampleBaseDir+"/pat/PATtuple_207_0_CEB.root",
  sampleBaseDir+"/pat/PATtuple_208_0_AJt.root",
  sampleBaseDir+"/pat/PATtuple_209_0_XTb.root",
  sampleBaseDir+"/pat/PATtuple_210_0_OWH.root",
  sampleBaseDir+"/pat/PATtuple_211_0_twe.root",
  sampleBaseDir+"/pat/PATtuple_212_0_yO8.root",
  sampleBaseDir+"/pat/PATtuple_213_0_seq.root",
  sampleBaseDir+"/pat/PATtuple_214_0_lN4.root",
  sampleBaseDir+"/pat/PATtuple_215_0_0Vt.root",
  sampleBaseDir+"/pat/PATtuple_216_0_dlH.root",
  sampleBaseDir+"/pat/PATtuple_217_0_EYq.root",
  sampleBaseDir+"/pat/PATtuple_218_0_zgC.root",
  sampleBaseDir+"/pat/PATtuple_219_0_ZCu.root",
  sampleBaseDir+"/pat/PATtuple_220_0_YiS.root",
  sampleBaseDir+"/pat/PATtuple_221_0_lN3.root",
  sampleBaseDir+"/pat/PATtuple_222_0_r4j.root",
  sampleBaseDir+"/pat/PATtuple_223_0_uvS.root",
  sampleBaseDir+"/pat/PATtuple_224_0_JCC.root",
  sampleBaseDir+"/pat/PATtuple_225_0_41o.root",
  sampleBaseDir+"/pat/PATtuple_226_0_6Dv.root",
  sampleBaseDir+"/pat/PATtuple_227_0_fl5.root",
  sampleBaseDir+"/pat/PATtuple_228_0_FFb.root",
  sampleBaseDir+"/pat/PATtuple_229_0_xhn.root",
  sampleBaseDir+"/pat/PATtuple_230_0_FzJ.root"
]

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "MC"
sampleRunMu = 0
