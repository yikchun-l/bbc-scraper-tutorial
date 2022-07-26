{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ef7ab103",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9dfaa9b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get(\"https://www.bbc.com/\")\n",
    "doc = BeautifulSoup(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "79698891",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/business-62305094\" rev=\"hero1|headline\">\n",
       "                                                                     EU allows get-out clause in Russian gas cut deal                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/world-us-canada-62308455\" rev=\"hero2|headline\">\n",
       "                                                                     US tops list of most known monkeypox cases                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/world-us-canada-62287198\" rev=\"hero3|headline\">\n",
       "                                                                     What did CIA boss say about Putin? Take our timed quiz                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/future/article/20220725-the-mystery-virus-that-protects-against-monkeypox\" rev=\"hero4|headline\">\n",
       "                                                                     The 83-year hunt for a vanished virus                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/travel/article/20220725-yucatans-abandoned-henequen-haciendas\" rev=\"hero5|headline\">\n",
       "                                                                     The forest of dilapidated mansions                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-europe-62308069\" rev=\"news|headline\">\n",
       "                                                                     Russia to pull out of International Space Station                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-latin-america-62292007\" rev=\"news|headline\">\n",
       "                                                                     Haiti gang violence kills more than 200 in 10 days                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/science-environment-62307383\" rev=\"news|headline\">\n",
       "                                                                     Covid origin studies say evidence points to market                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/sport/live/football/62302520\" rev=\"sport|headline\">\n",
       "                                                                     England v Sweden: Euro 2022 semi-final build-up                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/sport/football/62297849\" rev=\"sport|headline\">\n",
       "                                                                     Ronaldo set for Ten Hag talks to discuss future                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-australia-62301091\" rev=\"sport|headline\">\n",
       "                                                                     Pride jersey sparks player boycott in Australia                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-asia-62301385\" rev=\"regional-news|headline\">\n",
       "                                                                     US urges China to act on Myanmar after executions                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-asia-india-62262512\" rev=\"regional-news|headline\">\n",
       "                                                                     How India's digital revolution is connecting millions                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-asia-62301427\" rev=\"regional-news|headline\">\n",
       "                                                                     Japan executes Akihabara mass murderer                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-asia-62287815\" rev=\"regional-news|headline\">\n",
       "                                                                     Myanmar military executes activists and ex-MP                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/worklife/article/20220721-the-passive-aggressive-colleagues-who-poison-workplaces\" rev=\"editors-picks|headline\">\n",
       "                                                                     Why passive-aggressive staff are toxic                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/culture/article/20220725-why-are-we-so-fascinated-by-identical-twins\" rev=\"editors-picks|headline\">\n",
       "                                                                     The fascination of identical twins                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/future/article/20220720-do-octopuses-feel-pain\" rev=\"editors-picks|headline\">\n",
       "                                                                     Why octopuses probably have feelings                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/travel/article/20220724-the-cornish-farm-that-plans-to-last-1000-years\" rev=\"editors-picks|headline\">\n",
       "                                                                     The farmers rewilding a 'green desert'                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/entertainment-arts-62255561\" rev=\"editors-picks|headline\">\n",
       "                                                                     Mercury Prize: Find out all about this year's nominees                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/58888451\" rev=\"editors-picks|headline\">\n",
       "                                                                     Can the world cope without Russian oil and gas?                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/uk-politics-62300513\" rev=\"editors-picks|headline\">\n",
       "                                                                     No knockout blows, but Sunak is short of time                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/business-62289737\" rev=\"primary-special-features|headline\">\n",
       "                                                                     A mind-reading combat jet for the future                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/business-62235741\" rev=\"primary-special-features|headline\">\n",
       "                                                                     A look at the tech behind your coffee                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-us-canada-62301031\" rev=\"video|headline\">\n",
       "                                                                     People flee California's largest wildfire this year                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-us-canada-62301031\" rev=\"video|headline\">\n",
       "                                                                     People flee California's largest wildfire...                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-us-canada-62303581\" rev=\"video|headline\">\n",
       "                                                                     Wildfire tears through homes in Texas                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/uk-politics-62299315\" rev=\"video|headline\">\n",
       "                                                                     Our Next Prime Minister: Watch BBC debate...                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-us-canada-62300414\" rev=\"video|headline\">\n",
       "                                                                     The Great Salt Lake is running out of water                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/entertainment-arts-62287568\" rev=\"video|headline\">\n",
       "                                                                     Five things we learned at Comic-Con                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-62229602\" rev=\"video|headline\">\n",
       "                                                                     I travel the world with three cats on my...                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-asia-pacific-62260748\" rev=\"video|headline\">\n",
       "                                                                     Thai cave rescue: 'At first it was difficult'                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/10462520\" rev=\"video|headline\">\n",
       "                                                                     One-minute World News                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-africa-62270540\" rev=\"video|headline\">\n",
       "                                                                     Face to face with the bandit warlords of...                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/uk-62219752\" rev=\"video|headline\">\n",
       "                                                                     Afghan trans woman finds new home in Brighton                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/entertainment-arts-62301422\" rev=\"more-bbc|headline\">\n",
       "                                                                     Bucks Fizz star backs Cardiff to host Eurovision                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/health-61269586\" rev=\"more-bbc|headline\">\n",
       "                                                                     Cause of mystery child hepatitis outbreak found                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/science-environment-62253581\" rev=\"more-bbc|headline\">\n",
       "                                                                     UK cities warned to prepare for more wildfires                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/science-environment-62306617\" rev=\"more-bbc|headline\">\n",
       "                                                                     Eutelsat and OneWeb aim to combine operations                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/business-62288139\" rev=\"more-bbc|headline\">\n",
       "                                                                     Musk denies affair with Google co-founder's wife                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/science-environment-62291954\" rev=\"more-bbc|headline\">\n",
       "                                                                     Ancient fossil is earliest known animal predator                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/health-62279436\" rev=\"more-bbc|headline\">\n",
       "                                                                     WHO declares highest alert over monkeypox                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/business-61596047\" rev=\"secondary-special-features|headline\">\n",
       "                                                                     Whisky makers are turning their backs on peat                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"https://www.bbc.com/news/business-62220162\" rev=\"secondary-special-features|headline\">\n",
       "                                                                     The allotment firms helping trim long waiting lists                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/uk-england-suffolk-62290216\" rev=\"world-in-pictures1|headline\">\n",
       "                                                                     In pictures: Sheeran joins Snow Patrol at Latitude                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/uk-scotland-highlands-islands-62291116\" rev=\"world-in-pictures2|headline\">\n",
       "                                                                     In pictures: First Scottish tree hugging contest                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/world-europe-62285090\" rev=\"world-in-pictures3|headline\">\n",
       "                                                                     In pictures: Wildfires rage from Tenerife to Greece                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/uk-england-norfolk-62227836\" rev=\"world-in-pictures4|headline\">\n",
       "                                                                     'Underwater paradise' captured during heatwave                                                            </a>\n",
       " </h3>,\n",
       " <h3 class=\"media__title\">\n",
       " <a class=\"media__link\" href=\"/news/uk-england-norfolk-62255042\" rev=\"world-in-pictures5|headline\">\n",
       "                                                                     Drone images show homes gutted by heatwave blaze                                                            </a>\n",
       " </h3>]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Grab all of the titles\n",
    "titles = doc.select(\".media__title\")\n",
    "titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a74cd0cf",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EU allows get-out clause in Russian gas cut deal\n",
      "/news/business-62305094\n",
      "US tops list of most known monkeypox cases\n",
      "https://www.bbc.com/news/world-us-canada-62308455\n",
      "What did CIA boss say about Putin? Take our timed quiz\n",
      "https://www.bbc.com/news/world-us-canada-62287198\n",
      "The 83-year hunt for a vanished virus\n",
      "https://www.bbc.com/future/article/20220725-the-mystery-virus-that-protects-against-monkeypox\n",
      "The forest of dilapidated mansions\n",
      "https://www.bbc.com/travel/article/20220725-yucatans-abandoned-henequen-haciendas\n",
      "Russia to pull out of International Space Station\n",
      "/news/world-europe-62308069\n",
      "Haiti gang violence kills more than 200 in 10 days\n",
      "/news/world-latin-america-62292007\n",
      "Covid origin studies say evidence points to market\n",
      "/news/science-environment-62307383\n",
      "England v Sweden: Euro 2022 semi-final build-up\n",
      "/sport/live/football/62302520\n",
      "Ronaldo set for Ten Hag talks to discuss future\n",
      "/sport/football/62297849\n",
      "Pride jersey sparks player boycott in Australia\n",
      "/news/world-australia-62301091\n",
      "US urges China to act on Myanmar after executions\n",
      "/news/world-asia-62301385\n",
      "How India's digital revolution is connecting millions\n",
      "/news/world-asia-india-62262512\n",
      "Japan executes Akihabara mass murderer\n",
      "/news/world-asia-62301427\n",
      "Myanmar military executes activists and ex-MP\n",
      "/news/world-asia-62287815\n",
      "Why passive-aggressive staff are toxic\n",
      "https://www.bbc.com/worklife/article/20220721-the-passive-aggressive-colleagues-who-poison-workplaces\n",
      "The fascination of identical twins\n",
      "https://www.bbc.com/culture/article/20220725-why-are-we-so-fascinated-by-identical-twins\n",
      "Why octopuses probably have feelings\n",
      "https://www.bbc.com/future/article/20220720-do-octopuses-feel-pain\n",
      "The farmers rewilding a 'green desert'\n",
      "https://www.bbc.com/travel/article/20220724-the-cornish-farm-that-plans-to-last-1000-years\n",
      "Mercury Prize: Find out all about this year's nominees\n",
      "https://www.bbc.com/news/entertainment-arts-62255561\n",
      "Can the world cope without Russian oil and gas?\n",
      "https://www.bbc.com/news/58888451\n",
      "No knockout blows, but Sunak is short of time\n",
      "https://www.bbc.com/news/uk-politics-62300513\n",
      "A mind-reading combat jet for the future\n",
      "https://www.bbc.com/news/business-62289737\n",
      "A look at the tech behind your coffee\n",
      "https://www.bbc.com/news/business-62235741\n",
      "People flee California's largest wildfire this year\n",
      "/news/world-us-canada-62301031\n",
      "People flee California's largest wildfire...\n",
      "/news/world-us-canada-62301031\n",
      "Wildfire tears through homes in Texas\n",
      "/news/world-us-canada-62303581\n",
      "Our Next Prime Minister: Watch BBC debate...\n",
      "/news/uk-politics-62299315\n",
      "The Great Salt Lake is running out of water\n",
      "/news/world-us-canada-62300414\n",
      "Five things we learned at Comic-Con\n",
      "/news/entertainment-arts-62287568\n",
      "I travel the world with three cats on my...\n",
      "/news/world-62229602\n",
      "Thai cave rescue: 'At first it was difficult'\n",
      "/news/world-asia-pacific-62260748\n",
      "One-minute World News\n",
      "/news/10462520\n",
      "Face to face with the bandit warlords of...\n",
      "/news/world-africa-62270540\n",
      "Afghan trans woman finds new home in Brighton\n",
      "/news/uk-62219752\n",
      "Bucks Fizz star backs Cardiff to host Eurovision\n",
      "/news/entertainment-arts-62301422\n",
      "Cause of mystery child hepatitis outbreak found\n",
      "/news/health-61269586\n",
      "UK cities warned to prepare for more wildfires\n",
      "/news/science-environment-62253581\n",
      "Eutelsat and OneWeb aim to combine operations\n",
      "/news/science-environment-62306617\n",
      "Musk denies affair with Google co-founder's wife\n",
      "/news/business-62288139\n",
      "Ancient fossil is earliest known animal predator\n",
      "/news/science-environment-62291954\n",
      "WHO declares highest alert over monkeypox\n",
      "/news/health-62279436\n",
      "Whisky makers are turning their backs on peat\n",
      "https://www.bbc.com/news/business-61596047\n",
      "The allotment firms helping trim long waiting lists\n",
      "https://www.bbc.com/news/business-62220162\n",
      "In pictures: Sheeran joins Snow Patrol at Latitude\n",
      "/news/uk-england-suffolk-62290216\n",
      "In pictures: First Scottish tree hugging contest\n",
      "/news/uk-scotland-highlands-islands-62291116\n",
      "In pictures: Wildfires rage from Tenerife to Greece\n",
      "/news/world-europe-62285090\n",
      "'Underwater paradise' captured during heatwave\n",
      "/news/uk-england-norfolk-62227836\n",
      "Drone images show homes gutted by heatwave blaze\n",
      "/news/uk-england-norfolk-62255042\n"
     ]
    }
   ],
   "source": [
    "57\n",
    "for title in titles:\n",
    "    print(title.text.strip())\n",
    "    print(title.a[\"href\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8e85f1da",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#this needs to be a dataframe...so we're going to create a list of dictionaries\n",
    "bbc_headlines = []\n",
    "\n",
    "for title in titles:\n",
    "    row = {}\n",
    "    row['title'] = title.text.strip()\n",
    "    row['link'] = title.a['href']\n",
    "    \n",
    "    bbc_headlines.append(row)\n",
    "    \n",
    "headlines_220727 = pd.DataFrame(bbc_headlines)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0bc681d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "headlines_220727.to_csv('bbc-headlines-220727.csv', index= False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7dc6155d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#this is fine, but we can't keep doing this manually\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
