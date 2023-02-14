{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b6ffb517",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from IPython.display import display\n",
    "pd.set_option(\"display.max_row\",None)\n",
    "df = pd.read_csv(\"/home/hanzala/Development/Python_the_ultimate_course_2023/22. Pandas and Tabular Data Processing/data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cd39d239",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>names</th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hanzala</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ahmed</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Zara</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     names  age\n",
       "0  Hanzala   24\n",
       "1    Ahmed   29\n",
       "2     Zara   27"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f26eb355",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.9.13"
  },
  "vscode": {
   "interpreter": {
    "hash": "e4fe6e0daa6e2ff4707e521f617226dac5238e4505cdfd8fbc6db96461148b2a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
