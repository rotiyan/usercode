// -*- C++ -*-
//
// Package:    TDAna
// Class:      TDAna
// 
/**\class TDAna TDAna.cc AnalysisExamples/TDAna/src/TDAna.cc

 Description: <one line class summary>

 Implementation:
 This class shows how to access:
 - level 1 calorimetric quantities
 - offline corrected jets (calibration performed here)
 - offline corrected MET, depending on jets corrections
 - MC informations         <---------------------------------- to do
 - B tagging               <---------------------------------- to do

 Evaluates:
 - DPhimin between MET and closest (in phi) offline jet
 - association of MC partons to offline jets            <----- to do
 - association of btags to offline jets                 <----- to do

*/
//
// Original Author:  Marco De Mattia
//         Created:  Tue May  8 13:05:37 CEST 2007
// $Id: TDAna.h,v 1.3 2007/12/10 12:27:41 tosi Exp $
//
//

// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/InputTag.h"

// Root includes
// -------------
#include "TH1D.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TFile.h"

// Data includes
// -------------

// // // GCT and RCT data formats
// // #include "DataFormats/L1GlobalCaloTrigger/interface/L1GctCollections.h"
// // #include "DataFormats/L1GlobalCaloTrigger/interface/L1GctEtSums.h"
// // #include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"

// // L1Extra
// // #include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"
// #include "DataFormats/Candidate/interface/Candidate.h"
// #include "DataFormats/Candidate/interface/CandidateFwd.h"

// #include "DataFormats/L1Trigger/interface/L1EmParticle.h"
// #include "DataFormats/L1Trigger/interface/L1JetParticle.h"
// #include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
// #include "DataFormats/L1Trigger/interface/L1EtMissParticle.h"
// #include "DataFormats/L1Trigger/interface/L1ParticleMap.h"

// #include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"
// #include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"

// #include "FastSimulation/L1CaloTriggerProducer/interface/FastL1Region.h"
// // No BitInfos for release versions
// #include "FastSimDataFormats/External/interface/FastL1BitInfo.h"

// #include "Geometry/CaloTopology/interface/CaloTowerConstituentsMap.h"
// #include "DataFormats/Math/interface/Vector3D.h"

// // L1 Pixel
// // #include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
// // #include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
// // #include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
// // #include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"

// // #include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"
// // #include "Geometry/TrackerTopology/interface/RectangularPixelTopology.h"

// #include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
// #include "FWCore/Framework/interface/ESHandle.h"
// #include "DataFormats/GeometryVector/interface/GlobalPoint.h"
// #include "DataFormats/GeometryVector/interface/GlobalVector.h"
// #include "DataFormats/GeometryVector/interface/LocalVector.h"
// #include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
// #include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
// #include "TrackingTools/Records/interface/TransientRecHitRecord.h"
// #include "Geometry/TrackerGeometryBuilder/interface/GluedGeomDet.h"
// #include "DataFormats/DetId/interface/DetId.h" 
// #include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
// #include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
// #include "DataFormats/GeometryVector/interface/LocalPoint.h"
// #include "DataFormats/GeometryVector/interface/GlobalPoint.h"

// #include "DataFormats/TrackReco/interface/TrackFwd.h"
// #include "DataFormats/TrackReco/interface/Track.h"

// #include "AnalysisExamples/PixelJet/interface/PixelJet.h"

// // GenJets
// #include "DataFormats/JetReco/interface/GenJetCollection.h"
// #include "DataFormats/JetReco/interface/GenJet.h"

// // Calo MEt
// #include "DataFormats/METReco/interface/CaloMET.h"


// Associator for the jets
#include "AnalysisExamples/AnalysisClasses/interface/AssociatorEt.h"

// L1Trigger evaluator
#include "AnalysisExamples/AnalysisClasses/interface/L1Trig.h"
#include "AnalysisExamples/AnalysisClasses/interface/HiVariables.h"
#include "AnalysisExamples/AnalysisClasses/interface/MultiTH1F.h"
#include "AnalysisExamples/AnalysisClasses/interface/MultiTProfile.h"
#include "AnalysisExamples/AnalysisClasses/interface/MultiStack.h"
#include "AnalysisExamples/AnalysisClasses/interface/L1PixelTrig.h"

//
// class declaration
//

class TDAna : public edm::EDAnalyzer {
 public:
  explicit TDAna(const edm::ParameterSet&);
  ~TDAna();


 private:
  virtual void beginJob(const edm::EventSetup&) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

//   double PI_;

  int eventcounter_;

  // Declare as static so that only one exists, even if more
  // than one TDAna object is created
  static L1Trig L1Trigger;

  edm::ParameterSet conf_;
  TFile* OutputFile;

  // Declare here, since it does not have a default constructor
  // it will be initialized with an initialization list ( in
  // the TDAna constructor ).
  //  HiVariables HiVar;

  // Use a dynamic construction, or the TFile problem will crash the job
  // when moving from one input file to another.
  // The histograms must be created after the TFile is opened.
  HiVariables * HiVar;

  edm::InputTag cenJetLabel_;
  edm::InputTag forJetLabel_;
  edm::InputTag tauJetLabel_;
  edm::InputTag l1MEtLabel_;
  edm::InputTag offlineJetLabel_;
  edm::InputTag offlineMEtLabel_;
  edm::InputTag MCParticleLabel_;
  edm::InputTag simplePixelJetLabel_;
  edm::InputTag globalMuonLabel_;
  edm::InputTag simpleElectronLabel_;
  edm::InputTag simpleTauLabel_;
  edm::InputTag summaryLabel_;

  unsigned int numTkCut_;
  bool QCD_;
  std::string OutputEffFileName;

  TH1D * uncorr_JetPt_IC5_;
  TH1D * corr_JetPt_IC5_;
  TH1D * JetNumber_IC5_;

  TH1D * MEt_CorrIC5_Pt_;
  TH1D * MEt_CorrIC5_Phi_;
  TH1D * MEt_CorrIC5_SumEt_;
  TH1D * MEt_CorrIC5_mEtSig_;

  TH1D * PixelJet_dz_;
  TH1D * PixelJet_Num_;
  TH1D * PixelJet_Track_Num_;


  TH1D * DPhimin_;

  TH1D * NJets_;
  TH1D * UncorrSumEt_;
  TH1D * UncorrHt_;
  TH1D * CorrSumEt_;
  TH1D * CorrHt_;
  TH1D * GoodSumEt_;
  TH1D * GoodHt_;
  TH1D * GoodHt2_;
  TH1D * MEt_;
  TH1D * MEtSig_;
  TH1D * MEtSigNew_;
  TH1D * MEtDPM_;
  TH1D * MEtDP1_;
  TH1D * MEtDP2_;
  TH1D * MEtDP3_;
  TH1D * UncorrMEtSig_;
  TH1D * CorrMEtSig_;
  TH1D * M3best_;
  TH1D * Mwbest_;
  TH1D * Chi2mass_;
  TH1D * M45best_;
  TH1D * Chi2ext_;
  TH2D * MEx_SumEt_;
  TH1D * DP12_;
  TH1D * DPbb_;
  TH1D * M_others_;
  TH1D * Mbbnoh_;
  TH1D * DPbbnoh_;
  TH1D * M8_;
  TH1D * C8_;

  TH1D * NJetsS_;
  TH1D * UncorrSumEtS_;
  TH1D * UncorrHtS_;
  TH1D * CorrSumEtS_;
  TH1D * CorrHtS_;
  TH1D * GoodSumEtS_;
  TH1D * GoodHtS_;
  TH1D * GoodHt2S_;
  TH1D * MEtS_;
  TH1D * MEtSigS_;
  TH1D * MEtSigNewS_;
  TH1D * MEtDPMS_;
  TH1D * MEtDP1S_; 
  TH1D * MEtDP2S_;
  TH1D * MEtDP3S_;
  TH1D * UncorrMEtSigS_;
  TH1D * CorrMEtSigS_;
  TH1D * M3bestS_;
  TH1D * MwbestS_;
  TH1D * Chi2massS_;
  TH1D * M45bestS_;
  TH1D * Chi2extS_;
  TH2D * MEx_SumEtS_;
  TH1D * DP12S_;
  TH1D * DPbbS_;
  TH1D * M_othersS_;
  TH1D * MbbnohS_;
  TH1D * DPbbnohS_;
  TH1D * M8S_;
  TH1D * C8S_;

  TH1D * NJetsSS_;
  TH1D * UncorrSumEtSS_;
  TH1D * UncorrHtSS_;
  TH1D * CorrSumEtSS_;
  TH1D * CorrHtSS_;
  TH1D * GoodSumEtSS_;
  TH1D * GoodHtSS_;
  TH1D * GoodHt2SS_;
  TH1D * MEtSS_;
  TH1D * MEtSigSS_;
  TH1D * MEtSigNewSS_;
  TH1D * MEtDPMSS_;
  TH1D * MEtDP1SS_;
  TH1D * MEtDP2SS_;
  TH1D * MEtDP3SS_;
  TH1D * UncorrMEtSigSS_;
  TH1D * CorrMEtSigSS_;
  TH1D * M3bestSS_;
  TH1D * MwbestSS_;
  TH1D * Chi2massSS_;
  TH1D * M45bestSS_;
  TH1D * Chi2extSS_;
  TH2D * MEx_SumEtSS_;
  TH1D * DP12SS_;
  TH1D * DPbbSS_;
  TH1D * M_othersSS_;
  TH1D * MbbnohSS_;
  TH1D * DPbbnohSS_;
  TH1D * M8SS_;
  TH1D * C8SS_;

  TH1D * NJetsSSS_;
  TH1D * UncorrSumEtSSS_;
  TH1D * UncorrHtSSS_;
  TH1D * CorrSumEtSSS_;
  TH1D * CorrHtSSS_;
  TH1D * GoodSumEtSSS_;
  TH1D * GoodHtSSS_;
  TH1D * GoodHt2SSS_;
  TH1D * MEtSSS_;
  TH1D * MEtSigSSS_;
  TH1D * MEtSigNewSSS_;
  TH1D * MEtDPMSSS_;
  TH1D * MEtDP1SSS_;
  TH1D * MEtDP2SSS_;
  TH1D * MEtDP3SSS_;
  TH1D * UncorrMEtSigSSS_;
  TH1D * CorrMEtSigSSS_;
  TH1D * M3bestSSS_;
  TH1D * MwbestSSS_;
  TH1D * Chi2massSSS_;
  TH1D * M45bestSSS_;
  TH1D * Chi2extSSS_;
  TH2D * MEx_SumEtSSS_;
  TH1D * DP12SSS_;
  TH1D * DPbbSSS_;
  TH1D * M_othersSSS_;
  TH1D * MbbnohSSS_;
  TH1D * DPbbnohSSS_;
  TH1D * M8SSS_;
  TH1D * C8SSS_;
  TH1D * N4NJSSS_;
  TH1D * E4NJSSS_;

  TH2D * UncorrMEt_SumEt_;
  TH2D * CorrMEt_SumEt_; 
  TH2D * MEt_SumEt_; 
  TH2D * UncorrMEt_SumEtC_; 
  TH2D * CorrMEt_SumEtC_; 
  TH2D * MEt_SumEtC_; 
  TH2D * UncorrMEt_SumEtJ_; 
  TH2D * CorrMEt_SumEtJ_; 
  TH2D * MEt_SumEtJ_; 


  // Trigger efficiency counters
  // Multijet
  int Eff_;
  int Eff_et1_;
  int Eff_et2_;
  int Eff_et3_;
  int Eff_et4_;

  int Eff_cen_;
  int Eff_cen_et1_;
  int Eff_cen_et2_;
  int Eff_cen_et3_;
  int Eff_cen_et4_;

  int Eff_tau_;
  int Eff_tau_et1_;
  int Eff_tau_et2_;
  int Eff_tau_et3_;
  int Eff_tau_et4_;

  int Eff_for_;
  int Eff_for_et1_;
  int Eff_for_et2_;
  int Eff_for_et3_;
  int Eff_for_et4_;

  int Eff_nofor_;
  int Eff_nofor_et1_;
  int Eff_nofor_et2_;
  int Eff_nofor_et3_;
  int Eff_nofor_et4_;

  // MEt+Jet
  int Eff_MEtJet_;
  int Eff_MEtJet_cen_;
  int Eff_MEtJet_tau_;
  int Eff_MEtJet_for_;
  int Eff_MEtJet_nofor_;
  // Tau
  int Eff_tautrig_;
  int Eff_tautrig_single_;
  int Eff_tautrig_ditau_;

  // Offline
  int offlineEffMultijet_;
  int offlineEffMEtJet_;
  int offlineEffTauTrig_;

  double dz_;
  double dzmax_;
  int bins_;
  double dR_;
  double dRmax_;
  int jets_;
  int jetMin_;
  int jetMax_;

  float loose_;
  float medium_;
  float tight_;

  // Pixel trigger efficiency
  TH1D ** EffMultijetPixel_;
  TH1D ** EffMultijetPixelEt1_;
  TH1D ** EffMultijetPixelEt2_;
  TH1D ** EffMultijetPixelEt3_;
  TH1D ** EffMultijetPixelEt4_;
  TH1D ** EffMEtJetPixel_;
  int EffMultijetPixelSize_;
  int EffMultijetPixelSizeEt1_;
  int EffMultijetPixelSizeEt2_;
  int EffMultijetPixelSizeEt3_;
  int EffMultijetPixelSizeEt4_;
  int EffMEtJetPixelSize_;
  int ** EffMultijetPixelArray_;
  int ** EffMultijetPixelArrayEt1_;
  int ** EffMultijetPixelArrayEt2_;
  int ** EffMultijetPixelArrayEt3_;
  int ** EffMultijetPixelArrayEt4_;
  int ** EffMEtJetPixelArray_;

  // Offline efficiency
  TH1D ** offlineEffMultijetPixel_;
  TH1D ** offlineEffMEtJetPixel_;
  int offlineEffMultijetPixelSize_;
  int offlineEffMEtJetPixelSize_;
  int ** offlineEffMultijetPixelArray_;
  int ** offlineEffMEtJetPixelArray_;

  // Directory in the root file to hold the multiple histograms
  TDirectory *DirVertexDz_;

  // PixelTrigger alone efficiency
  int pixelTrig_3_;
  int pixelTrig_4_;
  int pixelTrig_5_;
  int pixelTrig_6_;

  int *numgoodpjeff_;
  int *numgoodpjeff_3_;
  int *numgoodpjeff_4_;
  int *numgoodpjeff_5_;
  int *numgoodpjeff_6_;

  TH1D * EffNumGoodPj_;
  TH1D * EffNumGoodPj_3_;
  TH1D * EffNumGoodPj_4_;
  TH1D * EffNumGoodPj_5_;
  TH1D * EffNumGoodPj_6_;

  // b tag discriminator histograms
  TH1D * deltaR;

  // PTag numbers
  // ------------
  double N0HETL[1000];
  double N1HETL[1000];
  double N0HETM[1000];
  double N1HETM[1000];
  double N0HETT[1000];
  double N1HETT[1000];
  double N0HPTL[1000];
  double N1HPTL[1000];
  double N0HPTM[1000];
  double N1HPTM[1000];
  double N0HPTT[1000];
  double N1HPTT[1000];

  double PHETL[1000];
  double PHETM[1000];
  double PHETT[1000];
  double PHPTL[1000];
  double PHPTM[1000];
  double PHPTT[1000];
  double PHETLS[1000];
  double PHETMS[1000];
  double PHETTS[1000];
  double PHPTLS[1000];
  double PHPTMS[1000];
  double PHPTTS[1000];

  double njsss;
  // ----------member data ---------------------------
};