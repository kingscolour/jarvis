
from jarvis.db.figshare import get_jid_data
from jarvis.core.atoms import Atoms
from jarvis.analysis.structure.spacegroup import Spacegroup3D
from jarvis.analysis.phonon.dos import PhononDos
#MgB2,JVASP-1151
phonon_dos=[2.121421220156185e-06, 2.684003727731897e-06, 5.617873068165091e-06, 1.2843555965188653e-05, 2.37883003268903e-05, 3.5896200126391746e-05, 4.8617357022187434e-05, 6.544570565535798e-05, 8.567110607629342e-05, 0.00010746793790811, 0.00013320449782628328, 0.00016411737859940278, 0.0001955670416938913, 0.00022619223995157023, 0.0002637090463383187, 0.0003116479621289142, 0.0003590690337943933, 0.0004009171954423605, 0.00045237180008597037, 0.0005165469157017062, 0.0005817233338994247, 0.0006447802847590051, 0.0007166084946309573, 0.0007970279236900905, 0.0008852293526986768, 0.0009817223576566547, 0.0010797870779971656, 0.0011845012190924388, 0.0013099150998840878, 0.001448857416475624, 0.0015896360728226912, 0.0017445429040744709, 0.0019315231667569321, 0.002139977385548371, 0.0023675078607728007, 0.0026305159862641024, 0.0029438920735715642, 0.00332007197619706, 0.003779866780383347, 0.004370296567102896, 0.005173722687343026, 0.006370836754490735, 0.00854133988100492, 0.0125161515550441, 0.01785896307063663, 0.021386196910071313, 0.01916527306339544, 0.011982143542564494, 0.005861905342292002, 0.003247455314437574, 0.003023971499723078, 0.003987587095572462, 0.006024985544482884, 0.008966735904802518, 0.011051251945530615, 0.010209563310170195, 0.006814957650150797, 0.0036529363258865194, 0.0024039824208209443, 0.0023266215065189783, 0.002692153607801722, 0.0032229415495713776, 0.0038990287544150184, 0.0048165224725605915, 0.006091744328338262, 0.007764670739770193, 0.009510400269587308, 0.01064483199172265, 0.01090052640506111, 0.010962681480211789, 0.011132115302646465, 0.010926042697083575, 0.009786268165575727, 0.008004913532468128, 0.006382426942234055, 0.005172908427181992, 0.004307963695874111, 0.0036835734215040347, 0.003285664969564971, 0.003121512520287006, 0.003210449971131561, 0.003520986572564207, 0.004019771237954181, 0.004725722368626457, 0.005638190141093609, 0.006850688630354374, 0.00847822408634607, 0.010417294227200408, 0.01196697019326355, 0.01245233534041992, 0.012004994345288978, 0.011331811561764419, 0.010887342060818598, 0.010522162128207517, 0.009965734479592356, 0.009253373621154918, 0.008555169330666676, 0.007993639737402702, 0.007551129728992674, 0.007122880608864726, 0.006542628233873626, 0.005529083236899104, 0.003966037882105103, 0.00225794447845699, 0.0010455439325071868, 0.0004406559053539256, 0.00022042479110581247, 0.00019070383493373735, 0.00027421409746159224, 0.00041774310300967776, 0.0005928691614428593, 0.0007867144353826526, 0.0010013616283067331, 0.0012463147488332201, 0.0015372382438704046, 0.0019057625523404395, 0.002390135995135087, 0.0029907870354617637, 0.0035302249668919005, 0.003721538335511281, 0.0035405052015870277, 0.0031994024711298466, 0.0029000358813633053, 0.0026987200849224076, 0.0025653194727916317, 0.0024648012266059644, 0.0023850839559181676, 0.002318831213138303, 0.0022630766133702154, 0.0022149277892167937, 0.0021723116610858836, 0.002134109987692688, 0.0020995365411062904, 0.0020680772980601657, 0.0020389383617055827, 0.002007969142698433, 0.0019563674646066475, 0.0018267573896959498, 0.0015186931503511293, 0.0010124090066334632, 0.0005067822096839554, 0.0001774300790881027, 3.9359351195835814e-05, 4.761519065663769e-06, 5.104693513516295e-07, 3.632528008305132e-08, 1.6280471953420905e-09, 3.440836417835123e-11, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
phonon_freq_cm=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600, 605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 680, 685, 690, 695, 700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790, 795, 800, 805, 810, 815, 820, 825, 830, 835, 840, 845, 850, 855, 860, 865, 870, 875, 880, 885, 890, 895, 900, 905, 910, 915, 920, 925, 930, 935, 940, 945, 950, 955, 960, 965, 970, 975, 980, 985, 990, 995]

def test_dos():
 ph=PhononDos(phonon_dos=phonon_dos, phonon_freq_cm=phonon_freq_cm)
 atoms=Spacegroup3D(Atoms.from_dict(get_jid_data(jid='JVASP-1151',dataset="dft_3d")['atoms'])).conventional_standard_structure
 print(ph.debye_temperature(atoms))
 print (ph.heat_capacity())
 print (ph.vibrational_entropy())
