sampleDataSet = '/DoubleMu/Run2011B-PromptReco-v1/AOD'
sampleNumEvents = 23929546 # according to DBS, as of 08 November 2011

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'GR_R_42_V21A::All'
sampleHLTProcess = '*'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON_MuonPhys.txt"

# restrict run range (mainly to get a sample with consistent trigger configuration)
sampleRunRange = [160000,999999]

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"

sampleRelease = "CMSSW_4_2_8_patch6" # original (i.e. RECO file) release,
                              # not the one we plan to process them with

sampleProcessRelease = "CMSSW_4_2_8_patch7" # release used to create new files with

sampleBaseDir = "dcap://dcap.pp.rl.ac.uk/pnfs/pp.rl.ac.uk/data/cms/store/user/"\
                +"harder/longlived/"+sampleProcessRelease+"/Data_Mu_Run2011B1"

sampleRecoFiles = []

samplePatFiles = [
  sampleBaseDir+"/pat/PATtuple_1_1_vUb.root",
  sampleBaseDir+"/pat/PATtuple_2_1_Cmr.root",
  sampleBaseDir+"/pat/PATtuple_3_1_5ku.root",
  sampleBaseDir+"/pat/PATtuple_4_1_m6E.root",
  sampleBaseDir+"/pat/PATtuple_5_1_Bcl.root",
  sampleBaseDir+"/pat/PATtuple_6_1_vGf.root",
  sampleBaseDir+"/pat/PATtuple_7_1_zkS.root",
  sampleBaseDir+"/pat/PATtuple_8_1_c8u.root",
  sampleBaseDir+"/pat/PATtuple_9_1_2XH.root",
  sampleBaseDir+"/pat/PATtuple_10_1_do1.root",
  sampleBaseDir+"/pat/PATtuple_11_1_1WC.root",
  sampleBaseDir+"/pat/PATtuple_12_1_I7V.root",
  sampleBaseDir+"/pat/PATtuple_13_1_UT4.root",
  sampleBaseDir+"/pat/PATtuple_14_1_lpE.root",
  sampleBaseDir+"/pat/PATtuple_15_1_aCZ.root",
  sampleBaseDir+"/pat/PATtuple_16_1_RVY.root",
  sampleBaseDir+"/pat/PATtuple_17_1_8Fs.root",
  sampleBaseDir+"/pat/PATtuple_18_1_E58.root",
  sampleBaseDir+"/pat/PATtuple_19_1_DFB.root",
  sampleBaseDir+"/pat/PATtuple_20_1_gQn.root",
  sampleBaseDir+"/pat/PATtuple_21_1_e75.root",
  sampleBaseDir+"/pat/PATtuple_22_1_Wtc.root",
  sampleBaseDir+"/pat/PATtuple_23_1_UmF.root",
  sampleBaseDir+"/pat/PATtuple_24_1_EnA.root",
  sampleBaseDir+"/pat/PATtuple_25_1_ZB9.root",
  sampleBaseDir+"/pat/PATtuple_26_1_Y1M.root",
  sampleBaseDir+"/pat/PATtuple_27_1_fRu.root",
  sampleBaseDir+"/pat/PATtuple_28_1_MlZ.root",
  sampleBaseDir+"/pat/PATtuple_29_1_vSS.root",
  sampleBaseDir+"/pat/PATtuple_30_1_JfN.root",
  sampleBaseDir+"/pat/PATtuple_31_1_ROh.root",
  sampleBaseDir+"/pat/PATtuple_32_1_bT1.root",
  sampleBaseDir+"/pat/PATtuple_33_1_F0I.root",
  sampleBaseDir+"/pat/PATtuple_34_1_iHp.root",
  sampleBaseDir+"/pat/PATtuple_35_1_zQp.root",
  sampleBaseDir+"/pat/PATtuple_36_1_ZP7.root",
  sampleBaseDir+"/pat/PATtuple_37_1_tpm.root",
  sampleBaseDir+"/pat/PATtuple_38_1_DGg.root",
  sampleBaseDir+"/pat/PATtuple_39_1_p2O.root",
  sampleBaseDir+"/pat/PATtuple_40_1_56E.root",
  sampleBaseDir+"/pat/PATtuple_41_1_iDC.root",
  sampleBaseDir+"/pat/PATtuple_42_1_ZAW.root",
  sampleBaseDir+"/pat/PATtuple_43_1_mT1.root",
  sampleBaseDir+"/pat/PATtuple_44_1_5a8.root",
  sampleBaseDir+"/pat/PATtuple_45_1_HHP.root",
  sampleBaseDir+"/pat/PATtuple_46_1_M7Y.root",
  sampleBaseDir+"/pat/PATtuple_47_1_dS7.root",
  sampleBaseDir+"/pat/PATtuple_48_1_MF0.root",
  sampleBaseDir+"/pat/PATtuple_49_1_zy9.root",
  sampleBaseDir+"/pat/PATtuple_50_1_Cpl.root",
  sampleBaseDir+"/pat/PATtuple_51_1_0xx.root",
  sampleBaseDir+"/pat/PATtuple_52_1_K9y.root",
  sampleBaseDir+"/pat/PATtuple_53_1_3wx.root",
  sampleBaseDir+"/pat/PATtuple_54_1_hhz.root",
  sampleBaseDir+"/pat/PATtuple_55_1_FHj.root",
  sampleBaseDir+"/pat/PATtuple_56_1_0GD.root",
  sampleBaseDir+"/pat/PATtuple_57_1_cHD.root",
  sampleBaseDir+"/pat/PATtuple_58_1_ev1.root",
  sampleBaseDir+"/pat/PATtuple_59_1_V6g.root",
  sampleBaseDir+"/pat/PATtuple_60_1_ah9.root",
  sampleBaseDir+"/pat/PATtuple_61_1_xvL.root",
  sampleBaseDir+"/pat/PATtuple_62_1_3Kc.root",
  sampleBaseDir+"/pat/PATtuple_63_1_ikS.root",
  sampleBaseDir+"/pat/PATtuple_64_1_3fh.root",
  sampleBaseDir+"/pat/PATtuple_65_1_P38.root",
  sampleBaseDir+"/pat/PATtuple_66_1_VoP.root",
  sampleBaseDir+"/pat/PATtuple_67_1_ojf.root",
  sampleBaseDir+"/pat/PATtuple_68_1_vqE.root",
  sampleBaseDir+"/pat/PATtuple_69_1_WEc.root",
  sampleBaseDir+"/pat/PATtuple_70_1_X56.root",
  sampleBaseDir+"/pat/PATtuple_71_1_2QM.root",
  sampleBaseDir+"/pat/PATtuple_72_1_LZe.root",
  sampleBaseDir+"/pat/PATtuple_73_1_RDV.root",
  sampleBaseDir+"/pat/PATtuple_74_1_eFR.root",
  sampleBaseDir+"/pat/PATtuple_75_1_A9u.root",
  sampleBaseDir+"/pat/PATtuple_76_1_j47.root",
  sampleBaseDir+"/pat/PATtuple_77_1_jBd.root",
  sampleBaseDir+"/pat/PATtuple_78_1_jwG.root",
  sampleBaseDir+"/pat/PATtuple_79_1_rbJ.root",
  sampleBaseDir+"/pat/PATtuple_80_1_Hfv.root",
  sampleBaseDir+"/pat/PATtuple_81_1_y8G.root",
  sampleBaseDir+"/pat/PATtuple_82_1_Mfh.root",
  sampleBaseDir+"/pat/PATtuple_83_1_reO.root",
  sampleBaseDir+"/pat/PATtuple_84_1_BG6.root",
  sampleBaseDir+"/pat/PATtuple_85_1_4C6.root",
  sampleBaseDir+"/pat/PATtuple_86_1_vHe.root",
  sampleBaseDir+"/pat/PATtuple_87_1_0H1.root",
  sampleBaseDir+"/pat/PATtuple_88_1_322.root",
  sampleBaseDir+"/pat/PATtuple_89_1_A1w.root",
  sampleBaseDir+"/pat/PATtuple_90_1_biK.root",
  sampleBaseDir+"/pat/PATtuple_91_1_eGY.root",
  sampleBaseDir+"/pat/PATtuple_92_1_8Bc.root",
  sampleBaseDir+"/pat/PATtuple_93_1_6Dt.root",
  sampleBaseDir+"/pat/PATtuple_94_1_Uer.root",
  sampleBaseDir+"/pat/PATtuple_95_1_byg.root",
  sampleBaseDir+"/pat/PATtuple_96_1_cvT.root",
  sampleBaseDir+"/pat/PATtuple_97_1_x5p.root",
  sampleBaseDir+"/pat/PATtuple_98_1_LVu.root",
  sampleBaseDir+"/pat/PATtuple_99_1_GP6.root",
  sampleBaseDir+"/pat/PATtuple_100_1_X3p.root",
  sampleBaseDir+"/pat/PATtuple_101_1_q60.root",
  sampleBaseDir+"/pat/PATtuple_102_1_tps.root",
  sampleBaseDir+"/pat/PATtuple_103_1_6aD.root",
  sampleBaseDir+"/pat/PATtuple_104_1_ZQG.root",
  sampleBaseDir+"/pat/PATtuple_105_1_FIc.root",
  sampleBaseDir+"/pat/PATtuple_106_1_CI1.root",
  sampleBaseDir+"/pat/PATtuple_107_1_YNK.root",
  sampleBaseDir+"/pat/PATtuple_108_1_cyv.root",
  sampleBaseDir+"/pat/PATtuple_109_1_LZn.root",
  sampleBaseDir+"/pat/PATtuple_110_1_CH0.root",
  sampleBaseDir+"/pat/PATtuple_111_1_30e.root",
  sampleBaseDir+"/pat/PATtuple_112_1_ix9.root",
  sampleBaseDir+"/pat/PATtuple_113_1_tTt.root",
  sampleBaseDir+"/pat/PATtuple_114_1_ZQb.root",
  sampleBaseDir+"/pat/PATtuple_115_1_a5i.root",
  sampleBaseDir+"/pat/PATtuple_116_1_Aaf.root",
  sampleBaseDir+"/pat/PATtuple_117_1_uCx.root",
  sampleBaseDir+"/pat/PATtuple_118_1_QRb.root",
  sampleBaseDir+"/pat/PATtuple_119_1_sSB.root",
  sampleBaseDir+"/pat/PATtuple_120_1_4mO.root",
  sampleBaseDir+"/pat/PATtuple_121_1_d2X.root",
  sampleBaseDir+"/pat/PATtuple_122_1_J5i.root",
  sampleBaseDir+"/pat/PATtuple_123_1_0eV.root",
  sampleBaseDir+"/pat/PATtuple_124_1_SWy.root",
  sampleBaseDir+"/pat/PATtuple_125_1_H0m.root",
  sampleBaseDir+"/pat/PATtuple_126_1_Z3M.root",
  sampleBaseDir+"/pat/PATtuple_127_1_39Z.root",
  sampleBaseDir+"/pat/PATtuple_128_1_eKE.root",
  sampleBaseDir+"/pat/PATtuple_129_1_Z5D.root",
  sampleBaseDir+"/pat/PATtuple_130_1_IPu.root",
  sampleBaseDir+"/pat/PATtuple_131_1_6tk.root",
  sampleBaseDir+"/pat/PATtuple_132_1_rPp.root",
  sampleBaseDir+"/pat/PATtuple_133_1_gG4.root",
  sampleBaseDir+"/pat/PATtuple_134_1_i0m.root",
  sampleBaseDir+"/pat/PATtuple_135_1_TGG.root",
  sampleBaseDir+"/pat/PATtuple_136_1_Bmj.root",
  sampleBaseDir+"/pat/PATtuple_137_1_bWx.root",
  sampleBaseDir+"/pat/PATtuple_138_1_zpd.root",
  sampleBaseDir+"/pat/PATtuple_139_1_9Zn.root",
  sampleBaseDir+"/pat/PATtuple_140_1_DJm.root",
  sampleBaseDir+"/pat/PATtuple_141_1_jAf.root",
  sampleBaseDir+"/pat/PATtuple_142_1_Aeq.root",
  sampleBaseDir+"/pat/PATtuple_143_1_kBD.root",
  sampleBaseDir+"/pat/PATtuple_144_1_0ob.root",
  sampleBaseDir+"/pat/PATtuple_145_1_n6l.root",
  sampleBaseDir+"/pat/PATtuple_146_1_GjV.root",
  sampleBaseDir+"/pat/PATtuple_147_1_C4V.root",
  sampleBaseDir+"/pat/PATtuple_148_1_AvE.root",
  sampleBaseDir+"/pat/PATtuple_149_1_KSq.root",
  sampleBaseDir+"/pat/PATtuple_150_1_tRx.root",
  sampleBaseDir+"/pat/PATtuple_151_1_CSm.root",
  sampleBaseDir+"/pat/PATtuple_152_1_lo1.root",
  sampleBaseDir+"/pat/PATtuple_153_1_fsa.root",
  sampleBaseDir+"/pat/PATtuple_154_1_6Sc.root",
  sampleBaseDir+"/pat/PATtuple_155_1_T51.root",
  sampleBaseDir+"/pat/PATtuple_156_1_7UM.root",
  sampleBaseDir+"/pat/PATtuple_157_1_TWW.root",
  sampleBaseDir+"/pat/PATtuple_158_1_tez.root",
  sampleBaseDir+"/pat/PATtuple_159_1_2Cy.root",
  sampleBaseDir+"/pat/PATtuple_160_1_507.root",
  sampleBaseDir+"/pat/PATtuple_161_1_VR6.root",
  sampleBaseDir+"/pat/PATtuple_162_1_ODc.root",
  sampleBaseDir+"/pat/PATtuple_163_1_GGr.root",
  sampleBaseDir+"/pat/PATtuple_164_1_vZB.root",
  sampleBaseDir+"/pat/PATtuple_165_1_MPM.root",
  sampleBaseDir+"/pat/PATtuple_166_1_GsR.root",
  sampleBaseDir+"/pat/PATtuple_167_1_QpF.root",
  sampleBaseDir+"/pat/PATtuple_168_1_BhI.root",
  sampleBaseDir+"/pat/PATtuple_169_1_Uk8.root",
  sampleBaseDir+"/pat/PATtuple_170_1_EDR.root",
  sampleBaseDir+"/pat/PATtuple_171_1_eEP.root",
  sampleBaseDir+"/pat/PATtuple_172_1_4Wg.root",
  sampleBaseDir+"/pat/PATtuple_173_1_XwI.root",
  sampleBaseDir+"/pat/PATtuple_174_1_nOr.root",
  sampleBaseDir+"/pat/PATtuple_175_0_XLH.root",
  sampleBaseDir+"/pat/PATtuple_176_0_oAF.root",
  sampleBaseDir+"/pat/PATtuple_177_0_AWl.root",
  sampleBaseDir+"/pat/PATtuple_178_0_2X2.root",
  sampleBaseDir+"/pat/PATtuple_179_0_cwj.root",
  sampleBaseDir+"/pat/PATtuple_180_0_xcB.root",
  sampleBaseDir+"/pat/PATtuple_181_0_wQ6.root",
  sampleBaseDir+"/pat/PATtuple_182_0_E3m.root",
  sampleBaseDir+"/pat/PATtuple_183_0_sEr.root",
  sampleBaseDir+"/pat/PATtuple_184_0_x5E.root",
  sampleBaseDir+"/pat/PATtuple_185_0_FBV.root",
  sampleBaseDir+"/pat/PATtuple_186_0_8Qm.root",
  sampleBaseDir+"/pat/PATtuple_187_0_ltF.root",
  sampleBaseDir+"/pat/PATtuple_188_0_BGE.root",
  sampleBaseDir+"/pat/PATtuple_189_0_ap7.root",
  sampleBaseDir+"/pat/PATtuple_190_0_Bgq.root",
  sampleBaseDir+"/pat/PATtuple_191_0_CnS.root",
  sampleBaseDir+"/pat/PATtuple_192_0_jKc.root",
  sampleBaseDir+"/pat/PATtuple_193_0_Y91.root",
  sampleBaseDir+"/pat/PATtuple_194_0_YNw.root",
  sampleBaseDir+"/pat/PATtuple_195_0_tW1.root",
  sampleBaseDir+"/pat/PATtuple_196_0_CTm.root",
  sampleBaseDir+"/pat/PATtuple_197_0_3s8.root",
  sampleBaseDir+"/pat/PATtuple_198_0_per.root",
  sampleBaseDir+"/pat/PATtuple_199_0_ibY.root",
  sampleBaseDir+"/pat/PATtuple_200_0_2bj.root",
  sampleBaseDir+"/pat/PATtuple_201_0_vbF.root",
  sampleBaseDir+"/pat/PATtuple_202_0_ShX.root",
  sampleBaseDir+"/pat/PATtuple_203_0_F49.root",
  sampleBaseDir+"/pat/PATtuple_204_0_apI.root",
  sampleBaseDir+"/pat/PATtuple_205_0_Zc9.root",
  sampleBaseDir+"/pat/PATtuple_206_0_fOE.root",
  sampleBaseDir+"/pat/PATtuple_207_0_o4t.root",
  sampleBaseDir+"/pat/PATtuple_208_0_ufp.root",
  sampleBaseDir+"/pat/PATtuple_209_0_nfn.root",
  sampleBaseDir+"/pat/PATtuple_210_0_0gY.root",
  sampleBaseDir+"/pat/PATtuple_211_0_zQK.root",
  sampleBaseDir+"/pat/PATtuple_212_0_kAz.root",
  sampleBaseDir+"/pat/PATtuple_213_0_G01.root",
  sampleBaseDir+"/pat/PATtuple_214_0_yv1.root",
  sampleBaseDir+"/pat/PATtuple_215_0_ubi.root",
  sampleBaseDir+"/pat/PATtuple_216_0_d0n.root",
  sampleBaseDir+"/pat/PATtuple_217_0_qfP.root",
  sampleBaseDir+"/pat/PATtuple_218_0_CfY.root",
  sampleBaseDir+"/pat/PATtuple_219_0_BiZ.root",
  sampleBaseDir+"/pat/PATtuple_220_0_fk2.root",
  sampleBaseDir+"/pat/PATtuple_221_0_VUo.root",
  sampleBaseDir+"/pat/PATtuple_222_0_bqR.root",
  sampleBaseDir+"/pat/PATtuple_223_0_0UR.root",
  sampleBaseDir+"/pat/PATtuple_224_0_NbO.root",
  sampleBaseDir+"/pat/PATtuple_225_0_qJs.root",
  sampleBaseDir+"/pat/PATtuple_226_0_qro.root",
  sampleBaseDir+"/pat/PATtuple_227_0_gQL.root",
  sampleBaseDir+"/pat/PATtuple_228_0_j91.root",
  sampleBaseDir+"/pat/PATtuple_229_0_jIj.root",
  sampleBaseDir+"/pat/PATtuple_230_0_Dl6.root",
  sampleBaseDir+"/pat/PATtuple_231_0_ZA2.root",
  sampleBaseDir+"/pat/PATtuple_232_0_83k.root",
  sampleBaseDir+"/pat/PATtuple_233_0_MZd.root",
  sampleBaseDir+"/pat/PATtuple_234_0_Cts.root",
  sampleBaseDir+"/pat/PATtuple_235_0_hBx.root",
  sampleBaseDir+"/pat/PATtuple_236_0_0gm.root",
  sampleBaseDir+"/pat/PATtuple_237_0_X90.root",
  sampleBaseDir+"/pat/PATtuple_238_0_zRd.root",
  sampleBaseDir+"/pat/PATtuple_239_0_sWY.root",
  sampleBaseDir+"/pat/PATtuple_240_0_AUG.root",
  sampleBaseDir+"/pat/PATtuple_241_0_btV.root",
  sampleBaseDir+"/pat/PATtuple_242_0_MfF.root",
  sampleBaseDir+"/pat/PATtuple_243_0_oqB.root",
  sampleBaseDir+"/pat/PATtuple_244_0_of9.root",
  sampleBaseDir+"/pat/PATtuple_245_0_Uok.root",
  sampleBaseDir+"/pat/PATtuple_246_0_N0B.root",
  sampleBaseDir+"/pat/PATtuple_247_0_Dv5.root",
  sampleBaseDir+"/pat/PATtuple_248_0_ydF.root",
  sampleBaseDir+"/pat/PATtuple_249_0_k28.root",
  sampleBaseDir+"/pat/PATtuple_250_0_lGP.root",
  sampleBaseDir+"/pat/PATtuple_251_0_Oux.root",
  sampleBaseDir+"/pat/PATtuple_252_0_4Wv.root",
  sampleBaseDir+"/pat/PATtuple_253_0_4Eu.root",
  sampleBaseDir+"/pat/PATtuple_254_0_F8d.root",
  sampleBaseDir+"/pat/PATtuple_255_0_I1X.root",
  sampleBaseDir+"/pat/PATtuple_256_0_x7N.root",
  sampleBaseDir+"/pat/PATtuple_257_0_D3V.root",
  sampleBaseDir+"/pat/PATtuple_258_0_d2r.root",
  sampleBaseDir+"/pat/PATtuple_259_0_EhY.root",
  sampleBaseDir+"/pat/PATtuple_260_0_h4M.root",
  sampleBaseDir+"/pat/PATtuple_261_0_jjM.root",
  sampleBaseDir+"/pat/PATtuple_262_0_TLl.root",
  sampleBaseDir+"/pat/PATtuple_263_0_IoD.root",
  sampleBaseDir+"/pat/PATtuple_264_0_AQt.root",
  sampleBaseDir+"/pat/PATtuple_265_0_EYP.root",
  sampleBaseDir+"/pat/PATtuple_266_0_3D7.root",
  sampleBaseDir+"/pat/PATtuple_267_0_pUE.root",
  sampleBaseDir+"/pat/PATtuple_268_0_2fj.root",
  sampleBaseDir+"/pat/PATtuple_269_0_u28.root",
  sampleBaseDir+"/pat/PATtuple_270_0_qlE.root",
  sampleBaseDir+"/pat/PATtuple_271_0_TeJ.root",
  sampleBaseDir+"/pat/PATtuple_272_0_MH2.root",
  sampleBaseDir+"/pat/PATtuple_273_0_wLc.root",
  sampleBaseDir+"/pat/PATtuple_274_0_QM5.root",
  sampleBaseDir+"/pat/PATtuple_275_0_dEX.root",
  sampleBaseDir+"/pat/PATtuple_276_0_Hxh.root",
  sampleBaseDir+"/pat/PATtuple_277_0_YGc.root",
  sampleBaseDir+"/pat/PATtuple_278_0_HPm.root",
  sampleBaseDir+"/pat/PATtuple_279_0_5b7.root",
  sampleBaseDir+"/pat/PATtuple_280_0_ylO.root",
  sampleBaseDir+"/pat/PATtuple_281_0_AhP.root",
  sampleBaseDir+"/pat/PATtuple_282_0_eVT.root",
  sampleBaseDir+"/pat/PATtuple_283_0_eWp.root",
  sampleBaseDir+"/pat/PATtuple_284_0_mKv.root",
  sampleBaseDir+"/pat/PATtuple_285_0_CgZ.root",
  sampleBaseDir+"/pat/PATtuple_286_0_41f.root",
  sampleBaseDir+"/pat/PATtuple_287_0_6ay.root",
  sampleBaseDir+"/pat/PATtuple_288_0_fLi.root",
  sampleBaseDir+"/pat/PATtuple_289_0_OXs.root",
  sampleBaseDir+"/pat/PATtuple_290_0_7Zh.root",
  sampleBaseDir+"/pat/PATtuple_291_0_8fk.root",
  sampleBaseDir+"/pat/PATtuple_292_0_UGx.root",
  sampleBaseDir+"/pat/PATtuple_293_0_qId.root",
  sampleBaseDir+"/pat/PATtuple_294_0_r3m.root",
  sampleBaseDir+"/pat/PATtuple_295_0_Omn.root",
  sampleBaseDir+"/pat/PATtuple_296_0_E7f.root",
  sampleBaseDir+"/pat/PATtuple_297_0_TzO.root",
  sampleBaseDir+"/pat/PATtuple_298_0_7vt.root",
  sampleBaseDir+"/pat/PATtuple_299_0_bjo.root",
  sampleBaseDir+"/pat/PATtuple_300_0_e0j.root",
  sampleBaseDir+"/pat/PATtuple_301_0_8hr.root",
  sampleBaseDir+"/pat/PATtuple_302_0_uO8.root",
  sampleBaseDir+"/pat/PATtuple_303_0_ZIa.root",
  sampleBaseDir+"/pat/PATtuple_304_0_9ZE.root",
  sampleBaseDir+"/pat/PATtuple_305_0_kH5.root",
  sampleBaseDir+"/pat/PATtuple_306_0_uT5.root",
  sampleBaseDir+"/pat/PATtuple_307_0_7vS.root",
  sampleBaseDir+"/pat/PATtuple_308_0_d9X.root",
  sampleBaseDir+"/pat/PATtuple_309_0_un3.root",
  sampleBaseDir+"/pat/PATtuple_310_0_BxD.root",
  sampleBaseDir+"/pat/PATtuple_311_0_lwS.root",
  sampleBaseDir+"/pat/PATtuple_312_0_IoY.root",
  sampleBaseDir+"/pat/PATtuple_313_0_AXc.root",
  sampleBaseDir+"/pat/PATtuple_314_0_iqo.root",
  sampleBaseDir+"/pat/PATtuple_315_0_bb3.root",
  sampleBaseDir+"/pat/PATtuple_316_0_89c.root",
  sampleBaseDir+"/pat/PATtuple_317_0_B4A.root",
  sampleBaseDir+"/pat/PATtuple_318_0_O4q.root",
  sampleBaseDir+"/pat/PATtuple_319_0_ndF.root",
  sampleBaseDir+"/pat/PATtuple_320_0_wnu.root",
  sampleBaseDir+"/pat/PATtuple_321_0_yVM.root",
  sampleBaseDir+"/pat/PATtuple_322_0_8q8.root",
  sampleBaseDir+"/pat/PATtuple_323_0_k5I.root",
  sampleBaseDir+"/pat/PATtuple_324_0_bhT.root",
  sampleBaseDir+"/pat/PATtuple_325_0_CWG.root",
  sampleBaseDir+"/pat/PATtuple_326_0_JUu.root",
  sampleBaseDir+"/pat/PATtuple_327_0_N0A.root",
  sampleBaseDir+"/pat/PATtuple_328_0_gl3.root",
  sampleBaseDir+"/pat/PATtuple_329_0_HBs.root",
  sampleBaseDir+"/pat/PATtuple_330_0_JWm.root",
  sampleBaseDir+"/pat/PATtuple_331_0_jmx.root",
  sampleBaseDir+"/pat/PATtuple_332_0_ZvW.root",
  sampleBaseDir+"/pat/PATtuple_333_0_OE8.root",
  sampleBaseDir+"/pat/PATtuple_334_0_Mnj.root",
  sampleBaseDir+"/pat/PATtuple_335_0_Oao.root",
  sampleBaseDir+"/pat/PATtuple_336_0_XrF.root",
  sampleBaseDir+"/pat/PATtuple_337_0_G3p.root",
  sampleBaseDir+"/pat/PATtuple_338_0_2nM.root",
  sampleBaseDir+"/pat/PATtuple_339_0_E3t.root",
  sampleBaseDir+"/pat/PATtuple_340_0_0SE.root",
  sampleBaseDir+"/pat/PATtuple_341_0_JRj.root",
  sampleBaseDir+"/pat/PATtuple_342_0_vV1.root",
  sampleBaseDir+"/pat/PATtuple_343_0_CIE.root",
  sampleBaseDir+"/pat/PATtuple_344_0_foU.root",
  sampleBaseDir+"/pat/PATtuple_345_0_vGS.root",
  sampleBaseDir+"/pat/PATtuple_346_0_jDi.root",
  sampleBaseDir+"/pat/PATtuple_347_0_NsJ.root",
  sampleBaseDir+"/pat/PATtuple_348_0_NeZ.root",
  sampleBaseDir+"/pat/PATtuple_349_0_bUO.root",
  sampleBaseDir+"/pat/PATtuple_350_0_6PL.root",
  sampleBaseDir+"/pat/PATtuple_351_0_p3x.root",
  sampleBaseDir+"/pat/PATtuple_352_0_0p0.root",
  sampleBaseDir+"/pat/PATtuple_353_0_hwM.root",
  sampleBaseDir+"/pat/PATtuple_354_0_ApB.root",
  sampleBaseDir+"/pat/PATtuple_355_1_Mj0.root",
  sampleBaseDir+"/pat/PATtuple_356_0_4by.root",
  sampleBaseDir+"/pat/PATtuple_357_0_eFp.root",
  sampleBaseDir+"/pat/PATtuple_358_0_ogK.root",
  sampleBaseDir+"/pat/PATtuple_359_0_xL6.root",
  sampleBaseDir+"/pat/PATtuple_360_0_RXa.root",
  sampleBaseDir+"/pat/PATtuple_361_0_eDJ.root",
  sampleBaseDir+"/pat/PATtuple_362_0_ZhS.root",
  sampleBaseDir+"/pat/PATtuple_363_0_oZX.root",
  sampleBaseDir+"/pat/PATtuple_364_0_e6O.root",
  sampleBaseDir+"/pat/PATtuple_365_0_O5b.root",
  sampleBaseDir+"/pat/PATtuple_366_0_3tx.root",
  sampleBaseDir+"/pat/PATtuple_367_0_rrL.root",
  sampleBaseDir+"/pat/PATtuple_368_0_ZVd.root",
  sampleBaseDir+"/pat/PATtuple_369_0_Mzp.root",
  sampleBaseDir+"/pat/PATtuple_370_0_ZFQ.root",
  sampleBaseDir+"/pat/PATtuple_371_1_yXz.root",
  sampleBaseDir+"/pat/PATtuple_372_0_oXL.root",
  sampleBaseDir+"/pat/PATtuple_373_0_wiK.root",
  sampleBaseDir+"/pat/PATtuple_374_0_bpv.root",
  sampleBaseDir+"/pat/PATtuple_375_1_uAN.root",
  sampleBaseDir+"/pat/PATtuple_376_1_XEU.root",
  sampleBaseDir+"/pat/PATtuple_377_1_RV5.root",
  sampleBaseDir+"/pat/PATtuple_378_1_Oq3.root",
  sampleBaseDir+"/pat/PATtuple_379_1_Xdj.root",
  sampleBaseDir+"/pat/PATtuple_380_1_hi2.root",
  sampleBaseDir+"/pat/PATtuple_381_1_qSl.root",
  sampleBaseDir+"/pat/PATtuple_382_1_wbu.root",
  sampleBaseDir+"/pat/PATtuple_383_1_Iu8.root",
  sampleBaseDir+"/pat/PATtuple_384_1_6ow.root",
  sampleBaseDir+"/pat/PATtuple_385_1_moe.root",
  sampleBaseDir+"/pat/PATtuple_386_1_o7C.root",
  sampleBaseDir+"/pat/PATtuple_387_1_PRn.root",
  sampleBaseDir+"/pat/PATtuple_388_1_MhP.root",
  sampleBaseDir+"/pat/PATtuple_389_1_h0M.root",
  sampleBaseDir+"/pat/PATtuple_390_1_58R.root",
  sampleBaseDir+"/pat/PATtuple_391_1_ds9.root",
  sampleBaseDir+"/pat/PATtuple_392_1_JoQ.root",
  sampleBaseDir+"/pat/PATtuple_393_1_yXs.root",
  sampleBaseDir+"/pat/PATtuple_394_1_wxA.root",
  sampleBaseDir+"/pat/PATtuple_395_1_Ba1.root",
  sampleBaseDir+"/pat/PATtuple_396_1_FBp.root",
  sampleBaseDir+"/pat/PATtuple_397_1_Iyj.root",
  sampleBaseDir+"/pat/PATtuple_398_1_1P8.root",
  sampleBaseDir+"/pat/PATtuple_399_1_YeV.root",
  sampleBaseDir+"/pat/PATtuple_400_1_ruN.root",
  sampleBaseDir+"/pat/PATtuple_401_1_sYL.root",
  sampleBaseDir+"/pat/PATtuple_402_1_VIR.root",
  sampleBaseDir+"/pat/PATtuple_403_1_xIH.root",
  sampleBaseDir+"/pat/PATtuple_404_1_DJA.root",
  sampleBaseDir+"/pat/PATtuple_405_1_YwP.root",
  sampleBaseDir+"/pat/PATtuple_406_1_wq5.root",
  sampleBaseDir+"/pat/PATtuple_407_1_3HR.root",
  sampleBaseDir+"/pat/PATtuple_408_1_vRQ.root",
  sampleBaseDir+"/pat/PATtuple_409_1_xpV.root",
  sampleBaseDir+"/pat/PATtuple_410_1_2yn.root"
    ]
