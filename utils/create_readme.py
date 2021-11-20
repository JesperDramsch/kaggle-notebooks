from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

# slug: [Description, Competition or Freestyle]
competition = {"intro-to-seismic-salt-and-how-to-geophysics": "Geophysics competition to identify salt bodies in seismic data. The competition was hosted by the seismic contractor TGS and provided patched seismic images with varying amounts of noise. The masks were provided as pixel-encoded masks to save bandwidth.",
                "intro-chest-xray-dicom-viz-u-nets-full-data": "Medical competition to identify pneumothorax in chest X-rays. Data provided in medical DICOM format. Very large images that benefit from downsampling.",
                "intro-to-santa-s-2019-viz-costs-22-s-and-search": "Fun kaggle competition to optimize allocation for families wanting to visit Santa's workshop. Optimization challenge where the global optimum was soon found.",
                "intro-to-connextx-env-and-minimax": "First reinforcement learning playground using Connect 4 on Kaggle to test new environment. Agents play against each other on the leaderboard. ConnectX is usually best approach by the Negamax algorithm, a Minimax variant.",
                "intro-to-deep-fakes-videos-and-metadata-eda": "Deep Fake competition to identify visual and sound manipulation usually using GANs in video footage.",
                "getting-started-with-standard-gans-tutorial": "Least Squares GAN on TPU to generate Monet painting from noise. Uses data augmentation to enrich the training set.",
                "understanding-and-improving-cyclegans-tutorial": "CycleGAN on TPUs to generate Monet painting from photographs. Uses Least Squares implementation of GANs to improve training and also implements some basic augmentation to get the competition going.",}

# slug: [Description, Competition or Freestyle]
freestyle = {"the-reason-we-re-happy": "Exploration of the 'World Happiness Report' data. Found a strong correlation of final score with wealth indicators. June winner in Reddit community [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/c89mz2/battle_dataviz_battle_for_the_month_of_july_2019/eskzdhd/).",
            "berlin-airbnbs-is-it-really-all-about-location": "AirBnB has been a source of income for many with a spare room, but become controversial due to commercial players buying apartments to rent out on the platform. In this analysis, we are looking at AirBnB data in Berlin, Germany. The questions are, what is the main influence on price of a rental. These questions are important for tourism, city planning, and renters alike. Where do affluent tourists rent AirBnBs? What decides a good price of your flat. Where can city planners accomodate for this new development of short term rental on the market?",}

## Sad times
correction = {}

medal = lambda num, corr: ["", "🥉", "🥈", "🥇"][(num >= 5) + (num >= 20) + (num >= 50) + corr]

string = """# Kaggle Notebooks
[![Kaggle Profile for Jesper Dramsch](https://img.shields.io/badge/kaggle-jesperdramsch-blue)](https:dramsch.net/kaggle)

Kaggle is an online community of data scientists and machine learning folks. It started out as a data science competition platform and has since evolved to incorporate datasets, courses, discussions, and of course notebooks. This is my place to showcase and store notebooks I made for kaggle.

[![notebook](https://road-to-kaggle-grandmaster.vercel.app/api/badges/jesperdramsch/notebook)](https://www.kaggle.com/jesperdramsch/notebooks)

## Competition Notebooks
"""

for name, info in competition.items():
    kernel = api.kernels_list(search=name)[0]
    badges = f"[![](https://img.shields.io/badge/view-notebook-orange)](notebooks-competition/{name}.ipynb) [![](https://img.shields.io/badge/open-colab-yellow)](https://colab.research.google.com/github/jesperdramsch/kaggle-notebooks/blob/master/notebooks-competition/{name}.ipynb) [![](https://img.shields.io/badge/kaggle-notebook-blue)](https://www.kaggle.com/jesperdramsch/{name})"
    string += f"### {medal(kernel.totalVotes, correction.get(name, 0))} {kernel.title} \n {badges}\n\n{info}\n\n"

string += "## Free-style Notebooks\n"
for name, info in freestyle.items():
    kernel = api.kernels_list(search=name)[0]
    badges = f"[![](https://img.shields.io/badge/view-notebook-orange)](notebooks-freestyle/{name}.ipynb) [![](https://img.shields.io/badge/open-colab-yellow)](https://colab.research.google.com/github/jesperdramsch/kaggle-notebooks/blob/master/notebooks-freestyle/{name}.ipynb) [![](https://img.shields.io/badge/kaggle-notebook-blue)](https://www.kaggle.com/jesperdramsch/{name})"
    string += f"### {medal(kernel.totalVotes, correction.get(name, 0))} {kernel.title} \n {badges}\n\n{info}\n\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(string)
