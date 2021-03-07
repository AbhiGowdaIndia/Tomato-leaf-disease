from tensorflow.keras.models import load_model
import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing import image
from PIL import Image,ImageOps

fin_model=load_model('Tomato_model_2.h5')
target_dict={0: 'Tomato___Bacterial_spot',
 1: 'Tomato___Early_blight',
 2: 'Tomato___Late_blight',
 3: 'Tomato___Leaf_Mold',
 4: 'Tomato___Septoria_leaf_spot',
 5: 'Tomato___Spider_mites Two-spotted_spider_mite',
 6: 'Tomato___Target_Spot',
 7: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 8: 'Tomato___Tomato_mosaic_virus',
 9: 'Tomato___healthy'}

caused_by={0:'Bacterial spot of peaches is caused by the bacteria "Xanthomonas campestris pv. pruni". Spots may form on the leaves and they can be mistaken for peach scab, which is caused by a fungus.',
              1:'Early blight caused by "Alternaria solani", it is a fungal pathogen. Early blight is the most destructive disease of tomatoes in the tropical and subtropical regions. Each 1% increase in intensity can reduce yield by 1.36%, and complete crop failure can occur when the disease is most severe.',
              2:'"Phytophthora infestans"it is an oomycete or water mold, a microorganism that causes the serious potato and tomato disease known as late blight. ',
              3:'"Passalora fulva" is a fungal plant pathogen that causes tomato leaf mold. Symptoms commonly occur on both sides of the foliage and sometimes on fruit. Older leaves are infected first and then the disease slowly moves up towards young leaves. ',
              4:'Septoria leaf spot is caused by "Septoria lycopersici", it a fungal pathogen.',
              5:'Spider mites are less than 1 mm (0.04 in) in size and vary in color. They generally live on the undersides of leaves of plants, where they may spin protective silk webs, and they can cause damage by puncturing the plant cells to feed.',
              6:'Target spot is caused by "Corynespora cassiicola", it a species of fungus well known as a plant pathogen.',
              7:'Tomato yellow leaf curl virus (TYLCV) is a DNA virus from the genus Begomovirus and the family Geminiviridae. TYLCV causes the most destructive disease of tomato, and it can be found in tropical and subtropical regions causing severe economic losses.',
              8:'Tomato mosaic virus (ToMV) is a plant pathogenic virus. It is found worldwide and affects tomatoes and many other plants.'
              }
symptoms={0:'Symptoms can be seen on the foliage, stems, and fruits of tomatoes. Initially small yellow-green lesions appear on young leaves for bacterial spot, whilst bacterial speck causes black spots with a narrow yellow halo. They are usually more numerous on leaf margins or tips, which may appear deformed and twisted.',
          1:'Symptoms of early blight occur on older foliage, stem, and fruits. Gray to brown spots appear on leaves and gradually grow in a concentric manner around a clear center - the characteristic “bullseye” formation. These lesions are surrounded by a bright yellow halo. As the disease progresses, entire leaves may turn chlorotic and shed, leading to significant defoliation. When leaves die and fall, fruits become more vulnerable to sun scald. ',
          2:'Brownish-green spots appear on the leaf margins and leaf tops. Later, large areas of the leaves turn brown completely. During wet weather, lesions on the lower side of the leaves may be covered with a gray to white moldy growth, making it easier to distinguish healthy from dead leaf tissue.',
          3:'Symptoms commonly occur on both sides of the foliage and sometimes on fruit. Older leaves are infected first and then the disease slowly moves up towards young leaves. On the upper leaf surface, small, diffuse, pale green or yellowish spots with indefinite margins appear. On the underside, olive green to grayish purple and velvety patches develop below the leaf spots. ',
          4:'Symptoms spread upwards from oldest to youngest growth. Small, water-soaked grey circular spots with dark-brown margins appear on the undersides of older leaves. At later stages of the disease, the spots enlarge and coalesce, and black dots appear in their centers. The same pattern may also be observed on stems and blossoms, but rarely on fruit.',
          5:'The spider mites feeding causes white to yellow speckles to form on the upper surface of the leaves. As infestation becomes more severe, leaves appear bronzed or silvery first and then become brittle, rip open between the leaf veins, and finally fall off. Spider mite eggs can be found on undersides of leaves. The spider mite itself is located there, nesting in a cocoon resembling webbing.',
          6:'The disease is identified by leaf damage taking the form of target-shaped spots with light centres and dark margins, as well as pits on the fruit.',
          7:'Infection at seedling stage results in  severe stunting of young leaves and shoots, leading to a somewhat bushy growth of the plant. In older plants, the infection results in excessive branching, thicker and wrinkled leaves, and interveinal chlorosis clearly visible on the leaf blade. At later stages of the disease, the plants take a leathery texture and their chlorotic margins are rolled upwards and inwards. If the infection takes place before the flowering stage, the number of fruits is considerably reduced, even though there are no noticeable symptoms on their surface.',
          8:'All plant parts can be affected during any growth stage. The symptoms depend on environmental conditions (light, day length, temperature). Infected leaves show a green and yellow mottling or a mosaic pattern. Younger leaves are slightly distorted. Older leaves show raised dark green areas. In some cases, dark necrotic streaks appear in stems and petioles. Plants are stunted to varying degrees and fruit set may be severely reduced. Unevenly ripening fruits develop brown spots on their surface, and internal, browning blotches in the fruit wall. Crop yield might be reduced significantly.'
          }
treatment={0:'Copper-containing bactericides can be used as a protectant and give partial disease control. Application at first sign of disease and then at 10 to 14-day intervals when warm (spot) / cold (speck), moist conditions prevail. As the development of resistance to copper is frequent, a combination of copper-based bactericide with mancozeb is also recommended.',
           1:'There are numerous fungicides on the market for controlling early blight. Fungicides based on or combinations of azoxystrobin, pyraclostrobin, difenoconazole, boscalid, chlorothalonil, fenamidone, maneb, mancozeb, trifloxystrobin, and ziram can be used. ',
           2:'Use fungicide sprays based on mandipropamid, chlorothalonil, fluazinam, mancozeb to combat late blight. Fungicides are generally needed only if the disease appears during a time of year when rain is likely or overhead irrigation is practiced.',
           3: 'Recommended compounds in field use are chlorothalonil, maneb, mancozeb and copper formulations. For greenhouses, difenoconazole, mandipropamid, cymoxanil, famoxadone and cyprodinil are recommended. ',
           4:'Fungicides containing maneb, mancozeb, chlorothalonil effectively control Septoria leaf spot. Apply at 7 to 10 day intervals throughout the season, mainly during flowering and fruit setting.',
           5:'Choose chemical control agents carefully so that they do not disrupt the population of predators. Fungicides based on wettable sulfur (3 g/l), spiromesifen (1 ml/l), dicofol (5 ml/l) or abamectin can be used for example (dilution in water). A second spray treatment application 2 to 3 days after the initial treatment is necessary.',
           6:'Use fungicide sprays based on mandipropamid, chlorothalonil, fluazinam, mancozeb to combat late blight. Fungicides are generally needed only if the disease appears during a time of year when rain is likely or overhead irrigation is practiced.',
           7:'Once infected with the virus, there are no treatments against the infection. Control the whitefly population to avoid the infection with the virus. Insecticides of the family of the pyrethroids used as soil drenches or spray during the seedling stage can reduce the population of whiteflies. However, their extensive use might promote resistance development in whitefly populations.',
           8:'Always consider an integrated approach with preventive measures together with biological treatments if available. There is no effective chemical treatment against Tomato Mosaic Virus.'}
def model_predict(img_path):
    size=(128,128)
    img = ImageOps.fit(img_path,size,Image.ANTIALIAS)
    # Preprocessing the image
    x = image.img_to_array(img)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
    pred=fin_model.predict(x)
    preds=np.argmax(pred)
    return preds


def main():
	st.title('Tomato leaf Disease Prediction using Deep Learning')
	st.write('Upload an image of tomato leaf to check whether it is a diseased tomato leaf or not.')

	html_temp="""
    <div style="background-color:tomato;padding:10px;">
    <h2 style="color:white;text-align:center;">Tomato leaf Disease Prediction</h2>
    </div>
    """
	st.markdown(html_temp,unsafe_allow_html=True)
	
	st.subheader("Upload Image")
	image_p= st.file_uploader("", type=['png','jpeg','jpg'])
	if image_p is not None:
		img=Image.open(image_p)
		st.image(img,width=240,height=240)
		if st.button("Predict"):
			result=model_predict(img)
			st.success('Result : "{}" category'.format(target_dict[result]))
			if result <9:
				st.subheader("Caused by :")
				st.error(caused_by[result])
				st.subheader("Symptoms :")
				st.warning(symptoms[result])
				st.subheader("Treatment :")
				st.info(treatment[result])
			else:
				st.info("This tomato leaf is a healthy leaf and does not have any disease.")
		
if __name__=='__main__':
	main()
