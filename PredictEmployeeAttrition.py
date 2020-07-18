{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Final Project\n",
    "### Nitish Ghosal\n",
    "### M12522228"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objective : Predicting Employee Attrition Using Machine Learning"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Description \n",
    "The dataset consists of 25491 obseravtions and 10 variables. Each row in dataset represents an employee; each column contains employee attributes:\n",
    "\n",
    "* satisfaction_level (0–1)\n",
    "* last_evaluation (Time since last evaluation in years)\n",
    "* number_projects (Number of projects completed while at work)\n",
    "* average_monthly_hours (Average monthly hours at workplace)\n",
    "* time_spend_company (Time spent at the company in years)\n",
    "* Work_accident (Whether the employee had a workplace accident)\n",
    "* left (Whether the employee left the workplace or not (1 or 0))\n",
    "* promotion_last_5years (Whether the employee was promoted in the last five years)\n",
    "* sales (Department in which they work for)\n",
    "* salary (Relative level of salary)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Approach\n",
    "We perform turnover analysis project by using Python’s Scikit-Learn library. We use Logistic Regression, Random Forest, and Support Vector Machine as classifier for employee attrition and measure the accuracy of models that are built."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 1 : Data Import and Preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Packages\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import os\n",
    "import re\n",
    "import sys,traceback\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Function to load the dataset'''\n",
    "def data_init(data_filepath):\n",
    "    try:\n",
    "        hr = pd.read_csv(data_filepath,low_memory= False)\n",
    "\n",
    "        col_list = list(hr)\n",
    "\n",
    "        print(\"Loaded successfully.\")\n",
    "    \n",
    "        return hr\n",
    "    except:\n",
    "        print(\"File Could not be loaded\")\n",
    "        print(\"Check your file or filepathname\")\n",
    "        return False\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter data filepath:C:\\Users\\nitis\\Desktop\\MS-BANA-Orientation-master\\MS-BANA-Orientation-master\\Day 1\\employee-attrition\\train.csv\n",
      "Loaded successfully.\n"
     ]
    }
   ],
   "source": [
    "'''User interacive way to access the dataset'''\n",
    "c = 1\n",
    "while (c!=0):\n",
    "    data_filepath = str(input(\"Enter data filepath:\"))\n",
    "    if os.path.isfile(data_filepath) :\n",
    "        hr_data = data_init(data_filepath)\n",
    "    else:\n",
    "        '''Add double slash in filepath and try again!'''\n",
    "        data_filepath = re.escape(data_filepath)\n",
    "        hr_data = data_init(data_filepath)\n",
    "    if type(hr_data) != str: c = 0\n",
    "    else: print (\"Check if file exists in the filepath and Let's try again ! \\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Column names:\n",
      "['satisfaction_level', 'last_evaluation_rating', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'left', 'promotion_last_5years', 'sales', 'salary']\n",
      "\n",
      "Sample data:\n"
     ]
    },
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
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation_rating</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>left</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "      <th>sales</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.8</td>\n",
       "      <td>5.3</td>\n",
       "      <td>3</td>\n",
       "      <td>167</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>8.0</td>\n",
       "      <td>8.6</td>\n",
       "      <td>6</td>\n",
       "      <td>272</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.1</td>\n",
       "      <td>8.8</td>\n",
       "      <td>8</td>\n",
       "      <td>282</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.7</td>\n",
       "      <td>5.2</td>\n",
       "      <td>3</td>\n",
       "      <td>169</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.1</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3</td>\n",
       "      <td>163</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   satisfaction_level  last_evaluation_rating  number_project  \\\n",
       "0                 3.8                     5.3               3   \n",
       "1                 8.0                     8.6               6   \n",
       "2                 1.1                     8.8               8   \n",
       "3                 3.7                     5.2               3   \n",
       "4                 4.1                     5.0               3   \n",
       "\n",
       "   average_montly_hours  time_spend_company  Work_accident  left  \\\n",
       "0                   167                   3              0     1   \n",
       "1                   272                   6              0     1   \n",
       "2                   282                   4              0     1   \n",
       "3                   169                   3              0     1   \n",
       "4                   163                   3              0     1   \n",
       "\n",
       "   promotion_last_5years  sales  salary  \n",
       "0                      0  sales     low  \n",
       "1                      0  sales  medium  \n",
       "2                      0  sales  medium  \n",
       "3                      0  sales     low  \n",
       "4                      0  sales     low  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Import Data\n",
    "hr = hr_data\n",
    "col_names = hr.columns.tolist()\n",
    "print(\"Column names:\")\n",
    "print(col_names)\n",
    "\n",
    "print(\"\\nSample data:\")\n",
    "hr.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "satisfaction_level        float64\n",
       "last_evaluation_rating    float64\n",
       "number_project              int64\n",
       "average_montly_hours        int64\n",
       "time_spend_company          int64\n",
       "Work_accident               int64\n",
       "left                        int64\n",
       "promotion_last_5years       int64\n",
       "department                 object\n",
       "salary                     object\n",
       "dtype: object"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Rename 'sales' column to department \n",
    "hr=hr.rename(columns = {'sales':'department'})\n",
    "#Display data type for each column\n",
    "hr.dtypes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "satisfaction_level        False\n",
       "last_evaluation_rating    False\n",
       "number_project            False\n",
       "average_montly_hours      False\n",
       "time_spend_company        False\n",
       "Work_accident             False\n",
       "left                      False\n",
       "promotion_last_5years     False\n",
       "department                False\n",
       "salary                    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Check for Missing Values\n",
    "hr.isnull().any()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The “left” column is the outcome variable recording 1 and 0. 1 for employees who left the company and 0 for those who didn’t."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(25491, 10)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Dimensions of our dataset\n",
    "hr.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
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
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation_rating</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>left</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>25491.000000</td>\n",
       "      <td>25491.000000</td>\n",
       "      <td>25491.000000</td>\n",
       "      <td>25491.000000</td>\n",
       "      <td>25491.000000</td>\n",
       "      <td>25491.000000</td>\n",
       "      <td>25491.000000</td>\n",
       "      <td>25491.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>6.137704</td>\n",
       "      <td>7.167832</td>\n",
       "      <td>4.215174</td>\n",
       "      <td>205.286846</td>\n",
       "      <td>3.497156</td>\n",
       "      <td>0.146012</td>\n",
       "      <td>0.234985</td>\n",
       "      <td>0.021419</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.486316</td>\n",
       "      <td>1.710754</td>\n",
       "      <td>1.324228</td>\n",
       "      <td>50.182916</td>\n",
       "      <td>1.457715</td>\n",
       "      <td>0.353125</td>\n",
       "      <td>0.423998</td>\n",
       "      <td>0.144780</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.900000</td>\n",
       "      <td>3.600000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>96.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.400000</td>\n",
       "      <td>5.600000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>160.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>6.500000</td>\n",
       "      <td>7.200000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>204.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>8.200000</td>\n",
       "      <td>8.700000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>249.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>10.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>320.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       satisfaction_level  last_evaluation_rating  number_project  \\\n",
       "count        25491.000000            25491.000000    25491.000000   \n",
       "mean             6.137704                7.167832        4.215174   \n",
       "std              2.486316                1.710754        1.324228   \n",
       "min              0.900000                3.600000        2.000000   \n",
       "25%              4.400000                5.600000        3.000000   \n",
       "50%              6.500000                7.200000        4.000000   \n",
       "75%              8.200000                8.700000        5.000000   \n",
       "max             10.000000               10.000000        8.000000   \n",
       "\n",
       "       average_montly_hours  time_spend_company  Work_accident          left  \\\n",
       "count          25491.000000        25491.000000   25491.000000  25491.000000   \n",
       "mean             205.286846            3.497156       0.146012      0.234985   \n",
       "std               50.182916            1.457715       0.353125      0.423998   \n",
       "min               96.000000            2.000000       0.000000      0.000000   \n",
       "25%              160.000000            3.000000       0.000000      0.000000   \n",
       "50%              204.000000            3.000000       0.000000      0.000000   \n",
       "75%              249.000000            4.000000       0.000000      0.000000   \n",
       "max              320.000000           10.000000       1.000000      1.000000   \n",
       "\n",
       "       promotion_last_5years  \n",
       "count           25491.000000  \n",
       "mean                0.021419  \n",
       "std                 0.144780  \n",
       "min                 0.000000  \n",
       "25%                 0.000000  \n",
       "50%                 0.000000  \n",
       "75%                 0.000000  \n",
       "max                 1.000000  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Summary for each variable\n",
    "hr.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The department column of the dataset has many categories and we need to reduce the categories for a better modeling. The department column has the following categories:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['sales', 'accounting', 'hr', 'technical', 'support', 'management',\n",
       "       'IT', 'product_mng', 'marketing', 'RandD'], dtype=object)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#To get the unique values for department\n",
    "hr['department'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let us combine “technical”, “support” and “IT” these three together and call them “technical”."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Combine \"technical\",\"support\" and \"IT\" into one department\n",
    "hr['department']=np.where(hr['department'] =='support', 'technical', hr['department'])\n",
    "hr['department']=np.where(hr['department'] =='IT', 'technical', hr['department'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After the change, this is how the department categories look:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sales' 'accounting' 'hr' 'technical' 'management' 'product_mng'\n",
      " 'marketing' 'RandD']\n"
     ]
    }
   ],
   "source": [
    "#Print the updated values of departments\n",
    "print(hr['department'].unique())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Exploration"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let us find out the number of employees who left the company and those who didn’t:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    19501\n",
       "1     5990\n",
       "Name: left, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr['left'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We observe that 5990 employees left the company, which is 23.4 per cent of the total employees in the organisation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
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
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation_rating</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>left</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6.668899</td>\n",
       "      <td>7.159582</td>\n",
       "      <td>4.198041</td>\n",
       "      <td>203.199836</td>\n",
       "      <td>3.378647</td>\n",
       "      <td>0.176247</td>\n",
       "      <td>0.026665</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.408347</td>\n",
       "      <td>7.194691</td>\n",
       "      <td>4.270952</td>\n",
       "      <td>212.081302</td>\n",
       "      <td>3.882972</td>\n",
       "      <td>0.047579</td>\n",
       "      <td>0.004341</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      satisfaction_level  last_evaluation_rating  number_project  \\\n",
       "left                                                               \n",
       "0               6.668899                7.159582        4.198041   \n",
       "1               4.408347                7.194691        4.270952   \n",
       "\n",
       "      average_montly_hours  time_spend_company  Work_accident  \\\n",
       "left                                                            \n",
       "0               203.199836            3.378647       0.176247   \n",
       "1               212.081302            3.882972       0.047579   \n",
       "\n",
       "      promotion_last_5years  \n",
       "left                         \n",
       "0                  0.026665  \n",
       "1                  0.004341  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr.groupby('left').mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Several observations:\n",
    "* The average satisfaction level of employees who stayed with the company is higher than that of the employees who left.\n",
    "* The average monthly work hours of employees who left the company is more than that of the employees who stayed.\n",
    "* The employees who had workplace accidents are less likely to leave than that of the employee who did not have workplace accidents.\n",
    "* The employees who were promoted in the last five years are less likely to leave than those who did not get a promotion in the last five years."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can calculate categorical means for categorical variables such as department and salary to get a more detailed sense of our data like so:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
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
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation_rating</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>left</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>department</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>RandD</th>\n",
       "      <td>6.186966</td>\n",
       "      <td>7.095356</td>\n",
       "      <td>4.250936</td>\n",
       "      <td>204.902622</td>\n",
       "      <td>3.361049</td>\n",
       "      <td>0.173783</td>\n",
       "      <td>0.153558</td>\n",
       "      <td>0.034457</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>accounting</th>\n",
       "      <td>5.835790</td>\n",
       "      <td>7.193845</td>\n",
       "      <td>4.224924</td>\n",
       "      <td>205.725684</td>\n",
       "      <td>3.530395</td>\n",
       "      <td>0.127660</td>\n",
       "      <td>0.265957</td>\n",
       "      <td>0.018237</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hr</th>\n",
       "      <td>6.037272</td>\n",
       "      <td>7.072720</td>\n",
       "      <td>4.078509</td>\n",
       "      <td>203.311657</td>\n",
       "      <td>3.357653</td>\n",
       "      <td>0.122125</td>\n",
       "      <td>0.283902</td>\n",
       "      <td>0.021412</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>management</th>\n",
       "      <td>6.218932</td>\n",
       "      <td>7.247423</td>\n",
       "      <td>4.262418</td>\n",
       "      <td>205.244611</td>\n",
       "      <td>4.299906</td>\n",
       "      <td>0.160262</td>\n",
       "      <td>0.134958</td>\n",
       "      <td>0.111528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>marketing</th>\n",
       "      <td>6.200756</td>\n",
       "      <td>7.165430</td>\n",
       "      <td>4.087973</td>\n",
       "      <td>203.987629</td>\n",
       "      <td>3.578694</td>\n",
       "      <td>0.158763</td>\n",
       "      <td>0.229553</td>\n",
       "      <td>0.050172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_mng</th>\n",
       "      <td>6.200727</td>\n",
       "      <td>7.185535</td>\n",
       "      <td>4.223910</td>\n",
       "      <td>203.686262</td>\n",
       "      <td>3.456407</td>\n",
       "      <td>0.149934</td>\n",
       "      <td>0.218626</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sales</th>\n",
       "      <td>6.164850</td>\n",
       "      <td>7.110125</td>\n",
       "      <td>4.183995</td>\n",
       "      <td>205.039581</td>\n",
       "      <td>3.541804</td>\n",
       "      <td>0.143984</td>\n",
       "      <td>0.240212</td>\n",
       "      <td>0.023519</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>technical</th>\n",
       "      <td>6.137237</td>\n",
       "      <td>7.212923</td>\n",
       "      <td>4.257805</td>\n",
       "      <td>206.091864</td>\n",
       "      <td>3.410974</td>\n",
       "      <td>0.145222</td>\n",
       "      <td>0.245317</td>\n",
       "      <td>0.008798</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             satisfaction_level  last_evaluation_rating  number_project  \\\n",
       "department                                                                \n",
       "RandD                  6.186966                7.095356        4.250936   \n",
       "accounting             5.835790                7.193845        4.224924   \n",
       "hr                     6.037272                7.072720        4.078509   \n",
       "management             6.218932                7.247423        4.262418   \n",
       "marketing              6.200756                7.165430        4.087973   \n",
       "product_mng            6.200727                7.185535        4.223910   \n",
       "sales                  6.164850                7.110125        4.183995   \n",
       "technical              6.137237                7.212923        4.257805   \n",
       "\n",
       "             average_montly_hours  time_spend_company  Work_accident  \\\n",
       "department                                                             \n",
       "RandD                  204.902622            3.361049       0.173783   \n",
       "accounting             205.725684            3.530395       0.127660   \n",
       "hr                     203.311657            3.357653       0.122125   \n",
       "management             205.244611            4.299906       0.160262   \n",
       "marketing              203.987629            3.578694       0.158763   \n",
       "product_mng            203.686262            3.456407       0.149934   \n",
       "sales                  205.039581            3.541804       0.143984   \n",
       "technical              206.091864            3.410974       0.145222   \n",
       "\n",
       "                 left  promotion_last_5years  \n",
       "department                                    \n",
       "RandD        0.153558               0.034457  \n",
       "accounting   0.265957               0.018237  \n",
       "hr           0.283902               0.021412  \n",
       "management   0.134958               0.111528  \n",
       "marketing    0.229553               0.050172  \n",
       "product_mng  0.218626               0.000000  \n",
       "sales        0.240212               0.023519  \n",
       "technical    0.245317               0.008798  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr.groupby('department').mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
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
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation_rating</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>left</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>salary</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>high</th>\n",
       "      <td>6.386124</td>\n",
       "      <td>7.049012</td>\n",
       "      <td>4.170743</td>\n",
       "      <td>203.784102</td>\n",
       "      <td>3.686736</td>\n",
       "      <td>0.153340</td>\n",
       "      <td>0.066792</td>\n",
       "      <td>0.060207</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>low</th>\n",
       "      <td>6.019963</td>\n",
       "      <td>7.180714</td>\n",
       "      <td>4.215674</td>\n",
       "      <td>205.429090</td>\n",
       "      <td>3.441506</td>\n",
       "      <td>0.144884</td>\n",
       "      <td>0.291945</td>\n",
       "      <td>0.008385</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>medium</th>\n",
       "      <td>6.222742</td>\n",
       "      <td>7.176300</td>\n",
       "      <td>4.223226</td>\n",
       "      <td>205.417351</td>\n",
       "      <td>3.523353</td>\n",
       "      <td>0.145868</td>\n",
       "      <td>0.203156</td>\n",
       "      <td>0.028644</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        satisfaction_level  last_evaluation_rating  number_project  \\\n",
       "salary                                                               \n",
       "high              6.386124                7.049012        4.170743   \n",
       "low               6.019963                7.180714        4.215674   \n",
       "medium            6.222742                7.176300        4.223226   \n",
       "\n",
       "        average_montly_hours  time_spend_company  Work_accident      left  \\\n",
       "salary                                                                      \n",
       "high              203.784102            3.686736       0.153340  0.066792   \n",
       "low               205.429090            3.441506       0.144884  0.291945   \n",
       "medium            205.417351            3.523353       0.145868  0.203156   \n",
       "\n",
       "        promotion_last_5years  \n",
       "salary                         \n",
       "high                 0.060207  \n",
       "low                  0.008385  \n",
       "medium               0.028644  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr.groupby('salary').mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Visualization"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let us visualize our data to get a much clearer picture of the data and the significant features."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2302787bba8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "#Bar chart for department employee work for and the frequency of turnover\n",
    "pd.crosstab(hr.department,hr.left).plot(kind='bar')\n",
    "plt.title('Turnover Frequency for Department')\n",
    "plt.xlabel('Department')\n",
    "plt.ylabel('Frequency of Turnover')\n",
    "plt.savefig('department_bar_chart')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is evident that the frequency of employee turnover depends a great deal on the department they work for. Thus, department can be a good predictor of the outcome variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x23027b4e3c8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Bar chart for employee salary level and the frequency of turnover\n",
    "table=pd.crosstab(hr.salary, hr.left)\n",
    "table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)\n",
    "plt.title('Stacked Bar Chart of Salary Level vs Turnover')\n",
    "plt.xlabel('Salary Level')\n",
    "plt.ylabel('Proportion of Employees')\n",
    "plt.savefig('salary_bar_chart')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The proportion of the employee turnover depends a great deal on their salary level; hence, salary level can be a good predictor in predicting the outcome."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
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
       "      <th>left</th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>department</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>RandD</th>\n",
       "      <td>1130</td>\n",
       "      <td>205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>accounting</th>\n",
       "      <td>966</td>\n",
       "      <td>350</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hr</th>\n",
       "      <td>903</td>\n",
       "      <td>358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>management</th>\n",
       "      <td>923</td>\n",
       "      <td>144</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>marketing</th>\n",
       "      <td>1121</td>\n",
       "      <td>334</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_mng</th>\n",
       "      <td>1183</td>\n",
       "      <td>331</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sales</th>\n",
       "      <td>5298</td>\n",
       "      <td>1675</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>technical</th>\n",
       "      <td>7977</td>\n",
       "      <td>2593</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "left            0     1\n",
       "department             \n",
       "RandD        1130   205\n",
       "accounting    966   350\n",
       "hr            903   358\n",
       "management    923   144\n",
       "marketing    1121   334\n",
       "product_mng  1183   331\n",
       "sales        5298  1675\n",
       "technical    7977  2593"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Proportion of employees left by department\n",
    "pd.crosstab(hr.department, hr.left)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABJQAAANeCAYAAABEflQZAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvNQv5yAAAIABJREFUeJzs3XuYZVV95//3R24SvACiFWyITcZ2RrQnaDrAxElS0Qw2mKR1ogZCBAxJxwxMdNIZBX+ZwahMSH4hxLu2QgCjIkPiQAQHCVpRM4KgEhHRoYWONE0gykVaE0zrd/7Yq/R0caq7Tt1Oner363nqqXPWXnvv7zqnau9zvnuttVNVSJIkSZIkSTP1qGEHIEmSJEmSpNFiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSZIkSZI0EBNKkiRJIyRJJXnqHNZ/XZI/n8+YJGkhJdmc5OeGHcdcLGQbkrwzyX9biG3PlyQ/kmRbkj2GHYvmjwklLTtJJpL8+pBj+KkkX9nJ8guTvHExY5IkjZ6lcE6TpFG3nD57Jzklyad6y6rqFVX1hmHF1M/UBFpVfa2qHlNV3x1mXJpfJpS06JKcmeSqKWW3TVN2/OJGNz+q6pNV9a8Xej9JxpNsWej9SNJSlGTPYceg6fn+SNLy5PFdk0woaRg+ATxnsrtjkh8G9gKePaXsqa3ujKTj37QkLRFJzkjy1SQPJflSkhcl2SfJA0me2VPviUn+KcmT2vOfT3JTq/d/kvzbnrqbk7wmyReAbyXZs99+eurvkeTcJF9PckeS09uQsT3b8scnOT/J3UnuSvLGXXXHb1eH/zbJeS3G25P8ZCu/M8m9SU7uqf/4JBcn+cckf5/k9ybPV5NXmpP8cZL7W4zHtmVnAz8FvLUNE3jrlDh+Isk9vR/sk/xSkptm8Pbs3WJ6KMktSdb0bOPprWfUA23ZL/Ys26HH1NQr5e21PS3JbcBt7dx8XntNHkzyhd73XpIGkeTIJJ9ux6e7k7w1yd5tWd/jTZL1wInAq9ux9K92sY8nJ/mLdsy+I8lv95T/U5IDe+o+q51f9kryr5J8LMk3Wtn7kuw/zT526DGVKReJpzuvJXk68E7g37W2PDDN9n4jyaYk9yW5IsmTe5ZVkleku3h/f5K3JckuXpPe8959wOt21t4k7wV+BPirFuerk6zMjuffiSRvaNt9KMlHkxzUs8+T2jnzG0n+W5bBsMflyC/fGoYb6BJIR7TnPw18HPjKlLKvVtXWdB/Sb2gnhhuS/OTkhtqB6Owkfwt8G/jR3h0lObidTH53ZwEleXmSW9vB7PYkvzll+bp0X26+2Q7ua1v5gUn+LMnWdkD+X6186knhWUk+17b/QeDRU7a/qy9Pv9va8WCSDyZ5dJL9gI8AT24H6m29JwtJWgK+SpcQeTzw+8CfAwcCfwmc0FPvpcDfVNW9SZ4NXAD8JvAE4F3AFUn26al/AvACYP+q2t5vP0kObnV/AziW7vzybOCFU2K8CNhOdxHjWcAxwEyGmB0FfKHF+H7gEuAn2nZ+lS4J9JhW9y0tth8FfgY4CXj5lG19BTgI+CPg/CSpqv8P+CRwehsmcHpvAFV1A/AN4D/0FP8q8N4ZxP+LLeb9gSuAtwIk2Qv4K+CjwJOA/wy8L8kgvW5f2Np0ON3r+dPA09q+frnFLEmz8V3gv9AdL/8d8DzgP7VlfY83VbUReB/wR+1Y+gvTbTxdsv+vgL8DVrTtvyrJ86tqK/Bp4Jd6VvkV4LKq+hcgwB8ATwaeDhwKvG6W7ex7XquqW4FXAJ9ubXlEwirJc1scLwUOBv6e7njf6+fpzlk/1uo9fwYxHQXcTnduOJudtLeqXgZ8DfiFFucfTbPNX6E7Hz4J2Bv43daGw4G30yUCD26vw4oZxKhFZkJJi66qvgNcT3fAp/3+JPCpKWWfaFcArgTeTPeh/U+AK5M8oWeTLwPWA4+lO2ACkGQl8DfAW6vqj3cR1r10B9bH0R3UzmtfakhyJHAx8F/pTk4/DWxu670X+CHgGXQHwvOmbjjdVZP/1eoeCPxPek5EM/zy9FJgLXAY8G+BU6rqW3Rfkra2A/Vj2olOkpaEqvqfVbW1qr5XVR8EbgOOpEvA9CaUfqWVQZcAeldVXV9V362qi4CHgaN76r+5qu6sqn/axX6gO36+qaq2VNX9wDmTG0kyRnccfVVVfauq7qU7js9kuPUdVfVnbS6ID9J9kH59VT1cVR8FvgM8NV1vp18Gzqyqh6pqM3Au3blr0t9X1bvbti6i+/A8NoMYaPV/tbXnQLovBe/f6RqdT1XVVW2f76X7UgHd6/wY4Jyq+k5VfQz4MDu+X7vyB1V1X3t//oXu/PxvgFTVrVV19wDbkqTvq6rPVtV1VbW9HU/fRZeoh/k53vwE8MSqen07Bt4OvJsfnBe+f/5qvXqOb2VU1aaquqadB/6R7nvLzzxiDzNr587Oa7tyInBBVX2uqh4GzqTr0bSyp845VfVAVX2N7sL+EY/czCNsraq3tNf+n+apvX9WVf+3nS8u7YnjxcBfVdWn2nfH/w7UgNvWIjChpGH5G36QPPopuoTSJ6eU/Q3dFejbquq97eD1AeDLQO+VhQur6pa2/F9a2eHABHBWuyqxU1V1ZVV9tTp/Q3dl9qfa4lPpDsrXtIP6XVX15Xb1+1jgFVV1f1X9S1t3qqPpemT9aatzGV0vrUkz/fK0taruo7tqMpODviQNVeuuPtn78gHgmXRXlT8G7JvkqCRPoTumfait9hRgw+Q6bb1D6a6ATrpzhvuhrXfnNOs+he74fHfPuu+iu0CwK/f0PJ5MbE0te0yLY296Lni0x71XWv9h8kFVfbs9fAwz8+fAL7TeUC8FPjnDL1D/0PP428Cj2zCEJwN3VtX3dhLvrnz/NW4JqbcCbwPuSbIxyeMG2JYkfV+SpyX5cJJ/SPJN4H/QjvfzdLx5Cl3v/95z0Gv5QZL/MrrkzJPpvrcU3XcYkjwpySXphk9/k+74fNAjdzGjdu7svLYrT6bnnFNV2+h6hvY979CdA2Zyzpl67p2P9k4Xxw7n7nZutHfrEmRCScPyCeDfJzmA7irAbcD/AX6ylT2z1dnhgNhM/WB7J490InAX3UF/l5Icm+S6dOOMHwCO4wcHxEPpup1OdShwX7vivTNPBu6qqt6sem+bZvLlaTYHfUkampYoejdwOvCE1i3/i3RXjb9HdyXyBLreSR+uqofaqncCZ1fV/j0/P9QuKEyqmeynVbkbOKRn3UN7Ht9Jl8A/qGdfj6uqZ8zLi9D5Ot1V86f0lP0I3TlqJnZ6Rbaq7qIbgvEiul5PMxnutjNbgUOz45yEvfF+i65n7qQf7hfWlBjfXFU/Tteb92l0PX4laTbeQXdxeVVVPY4u2fP9+X92cryZae+WO+l6oPaegx5bVce17T9Ad+H5pXTnrw/0fMb/g7aff9ti+9Xe2KaY9lg6g/PartqylZ5zTpsm4wnM/Lwznan73VV759KjaIdzd5J96dqgJcaEkobl03RjYdcDfwtQVd+kOwCup+tSeQdTDojN1A/i/Q5Wr6P7EP/+7Hpy1X2AvwD+GBhrB+2r+MEB8U7gX/VZ9U7gwEwz2V6Pu4EVrVtsbxt6t7OrL0/TseunpKVqP7pj1D9CN1cd3cWCSe+nGwp2IjsO0Xo38IrWeylJ9kvygiSPneV+LgVemWRFO16/ZnJB68nzUeDcJI9L8qh0k4zOaohCP21I2aXA2Uke274o/A7dldyZuIcp8wP2cTHwamA1P+jpNVvX033ReXW6SWbH6XoFT86/cRPwH5P8UJKn0vXinVa6icOPanMzfQv4Z7o5UCRpNh4LfBPYluTfAL81uWAXx5uZHEsBPgN8M93NH/ZNd2OHZyb5iZ4676ebC++X2PH89VhgG/BAkhXsPHl+E3BcuvlYfxh4Vc+yXZ3X7gEOadNq9PN+4OVJjmjfc/4HcH0bIjifdtXemb7m/VxG1/v2J1s7f5/pk3MaIhNKGoo2TvZGug/Vn+xZ9KlWNnl3t6uApyX5lXR38vlluuFsH97FLv4FeAndAfm92fnd3/YG9qE7aG9Pd3edY3qWn093UH5e+7KxIsm/aV9EPgK8PckB7YP3Tz9y83yabsLX325t+I/sOAZ60C9Pve4BnpDk8TOoK0mLpqq+RDdX0KfpjlWraRcQ2vLJxMWT6Y6lk+U30g0FfitwP7AJOGW2+6E7xn6UbgLtz9OdV7bzgy8ZJ9GdB77U9ncZ3RxG8+k/07X1drrz3Pvp5s6biTcBL05344c3T1PnQ3QXXz5U3fx6s9bmqvhFuiHdX6ebFPWkqvpyq3Ie3fxQ99DN3/S+XWzycXTvwf10vXO/QXcBR5Jm43fpegY9RHds+WDPsp0db84HDm+jAf7XdBtvFwF+gW4o9h10x8H30F0In3QFsAq4p6r+rqf89+lu/vAg3Rywf7mTdryXbuLvzXTnqO+3YwbntY8BtwD/kOTrfdpwLfDf6C6Y3013YXwmcwMOalft/QPg99prvtMbJE1VVbfQnTsvoWvDQ3Rz3j4816A1v7LjKBxp8ST5A+AM4Mer6nOt7KV0B9RXVNW7Wtm/p/tA/VS6LxavrKpPtWUTwJ9X1Xt6tvv9siSPpks+bQF+bcqcEL2xnEY32ds+dHMU7QVsqqrfa8tfRHfQPIzuwH5aVV2dbgLU8+gmzN4b+HhV/cd2RffPq+qQtv4auhPcU+m+zEA3N9Tk9tcCb6A7Of0T3ReOX6uqh5JsBn69qv661X0d8NSqmpyE9QJgHbAHcHg5MbckTatdNHhnVU3t/TrSknwV+M3Jc4UkSctFunkCH6Ab6njHsOPRD5hQkiRJy1abd+Fn6a4Aj9Fdsb2uql610xVHSJJfAv4QeNp0F04kSRolSX4BuJZuqNu5wFHAs8sExpLikDdJkrScha6H6f10Q95upeuRuvOVkncm2dbn550LHO9AWq/cd9D1nP1eT/lHpon/tUMLVpKWgCQ/Ms3xcVuSH9n1FpanJXjeW0c3n+5WulEcx5tMWnrsoaTdRpJt0yw6tqo+Oc0ySZIkSZI0hQklSZIkSZIkDWTPYQcwWwcddFCtXLly4PW+9a1vsd9++81/QEvEcm8fLP822r7RN9s2fvazn/16VT1xAULSNGZ7Lulnd/jbno5tt+27m6Xcds8li28+zyWzsZT/Hvsx3oVlvAtrd4l3pueSkU0orVy5khtvvHHg9SYmJhgfH5//gJaI5d4+WP5ttH2jb7ZtTPL38x+Ndma255J+doe/7enY9vFhhzEUtn182GH05blk8c3nuWQ2lvLfYz/Gu7CMd2HtLvHO9FzipNySJEmSJEkaiAklSZIkSZIkDcSEkiRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkjTykuyR5PNJPtyeH5bk+iS3Jflgkr1b+T7t+aa2fGXPNs5s5V9J8vzhtESSRoMJJUmSJEnLwSuBW3ue/yFwXlWtAu4HTm3lpwL3V9VTgfNaPZIcDhwPPANYC7w9yR6LFLskjRwTSpIkSZJGWpJDgBcA72nPAzwXuKxVuQh4YXu8rj2nLX9eq78OuKSqHq6qO4BNwJGL0wJJGj0mlCRJkiSNuj8FXg18rz1/AvBAVW1vz7cAK9rjFcCdAG35g63+98v7rCNJmmLPYQew2G6+60FOOePKRdvf5nNesGj7kiRpPqwc8Dy5YfX2OZ1bPVdKmoskPw/cW1WfTTI+Wdynau1i2c7WmbrP9cB6gLGxMSYmJgYJeV5t27ZtqPufzs13Pdi3fGxfeMv7Lp/3/a1e8fh53yYs3dd3Osa7sIx3R7tdQkmSJEnSsvIc4BeTHAc8GngcXY+l/ZPs2XohHQJsbfW3AIcCW5LsCTweuK+nfFLvOjuoqo3ARoA1a9bU+Pj4fLdpxiYmJhjm/qcz3YWGDau3c+7N8/81dPOJ4/O+TVi6r+90jHdhGe+OHPImSZIkaWRV1ZlVdUhVraSbVPtjVXUi8HHgxa3aycBkt5gr2nPa8o9VVbXy49td4A4DVgGfWaRmSNLIsYeSJEmSpOXoNcAlSd4IfB44v5WfD7w3ySa6nknHA1TVLUkuBb4EbAdOq6rvLn7YkjQaTChJkiRJWhaqagKYaI9vp89d2qrqn4GXTLP+2cDZCxehJC0fDnmTJEmSJEnSQEwoSZIkSZIkaSAmlCRJkiRJkjQQE0qSJEmSJEkaiAklSZIkSZIkDcSEkiRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgu0woJTk0yceT3JrkliSvbOUHJrkmyW3t9wGtPEnenGRTki8keXbPtk5u9W9LcnJP+Y8nubmt8+YkWYjGSpIkSZIkae5m0kNpO7Chqp4OHA2cluRw4Azg2qpaBVzbngMcC6xqP+uBd0CXgALOAo4CjgTOmkxCtTrre9ZbO/emSZIkSZIkaSHsMqFUVXdX1efa44eAW4EVwDrgolbtIuCF7fE64OLqXAfsn+Rg4PnANVV1X1XdD1wDrG3LHldVn66qAi7u2ZYkSZIkSZKWmD0HqZxkJfAs4HpgrKruhi7plORJrdoK4M6e1ba0sp2Vb+lT3m//6+l6MjE2NsbExMQg4QMwti9sWL194PVmazYxzsW2bdsWfZ+Lbbm30faNvt2hjZIkSZJ2bzNOKCV5DPAXwKuq6ps7meao34KaRfkjC6s2AhsB1qxZU+Pj47uI+pHe8r7LOffmgfJoc7L5xPFF2xd0CazZvC6jZLm30faNvt2hjZIkSZJ2bzO6y1uSveiSSe+rqr9sxfe04Wq03/e28i3AoT2rHwJs3UX5IX3KJUmSJEmStATN5C5vAc4Hbq2qP+lZdAUweae2k4HLe8pPand7Oxp4sA2Nuxo4JskBbTLuY4Cr27KHkhzd9nVSz7YkSZIkSZK0xMxk7NdzgJcBNye5qZW9FjgHuDTJqcDXgJe0ZVcBxwGbgG8DLweoqvuSvAG4odV7fVXd1x7/FnAhsC/wkfYjSZIkSZKkJWiXCaWq+hT95zkCeF6f+gWcNs22LgAu6FN+I/DMXcUiSVqekuwB3AjcVVU/n+Qw4BLgQOBzwMuq6jtJ9qG7G+iPA98AfrmqNrdtnAmcCnwX+O2qunrxWyJJWmxJHg18AtiH7vvNZVV1VpILgZ8BHmxVT6mqm9qoiDfRXQT/div/XNvWycDvtfpvrKqLkCT1NaM5lCRJWmCvBG7tef6HwHlVtQq4ny5RRPt9f1U9FTiv1SPJ4cDxwDOAtcDbW5JKkrT8PQw8t6p+DDgCWNum3gD4r1V1RPuZHG1xLLCq/awH3gGQ5EDgLOAo4EjgrDZVhySpDxNKkqShSnII8ALgPe15gOcCl7UqFwEvbI/Xtee05c9r9dcBl1TVw1V1B92w6yMXpwWSpGGqzrb2dK/20/eu0c064OK23nXA/u0mQ88Hrqmq+6rqfuAauosUkqQ+ZjKHkiRJC+lPgVcDj23PnwA8UFXb2/MtwIr2eAVwJ0BVbU/yYKu/AriuZ5u96+wgyXq6K9KMjY0xMTExL43Ytm3bvG1r2Das3r7rSj3G9h18nV6j/Lotp/d9ULZ9YthhqEfrlfpZ4KnA26rq+iS/BZyd5L8D1wJnVNXD9JxLmslzxnTlkqQ+TChJkoYmyc8D91bVZ5OMTxb3qVq7WLazdXYsrNoIbARYs2ZNjY+P96s2sImJCeZrW8N2yhlXDlR/w+rtnHvz7D9SbD5xfNbrDttyet8H1dv2lQP+zczV5nNesKj7m2p3ft+Xqqr6LnBEkv2BDyV5JnAm8A/A3nTH/dcAr2ceziULdXFiNpZqgnO6Cw1zvQgxnYV6DZbq6zsd411YxrsjE0qSpGF6DvCLSY4DHg08jq7H0v5J9my9lA4Btrb6W4BDgS1J9gQeD9zXUz6pdx1J0m6iqh5IMgGsrao/bsUPJ/kz4Hfb8+nOGVuA8SnlE9PsZ0EuTszGUk1wTndxYq4XIaazUBcnlurrOx3jXVjGuyPnUJIkDU1VnVlVh1TVSrpJtT9WVScCHwde3KqdDFzeHl/RntOWf6zdXfQK4Pgk+7Q7xK0CPrNIzZAkDVGSJ7aeSSTZF/g54MttXqTJufleCHyxrXIFcFI6RwMPVtXdwNXAMUkOaJNxH9PKJEl92ENJkrQUvQa4JMkbgc8D57fy84H3JtlE1zPpeICquiXJpcCXgO3AaW34gyRp+TsYuKjNo/Qo4NKq+nCSjyV5It1QtpuAV7T6VwHH0d3A4dvAywGq6r4kbwBuaPVeX1X3LWI7JGmkmFCSJC0JVTVBG1pQVbfT5y5tVfXPwEumWf9s4OyFi1CStBRV1ReAZ/Upf+409Qs4bZplFwAXzGuAkrRMOeRNkiRJkiRJA7GHkiRJkiRJGqrd7Y6hy4E9lCRJkiRJkjQQE0qSJEmSJEkaiAklSZIkSZIkDcSEkiRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSZIkSZI0EBNKkiRJkiRJGogJJUmSJEmSJA3EhJIkSZIkSZIGsuewA5AkSZIkSVruVp5x5aLu78K1+y3o9u2hJEmSJEmSpIGYUJIkSZIkSdJATChJkiRJkiRpICaUJEmSJI20JI9O8pkkf5fkliS/38oPS3J9ktuSfDDJ3q18n/Z8U1u+smdbZ7byryR5/nBaJElLnwklSZIkSaPuYeC5VfVjwBHA2iRHA38InFdVq4D7gVNb/VOB+6vqqcB5rR5JDgeOB54BrAXenmSPRW2JJI0IE0qSJEmSRlp1trWne7WfAp4LXNbKLwJe2B6va89py5+XJK38kqp6uKruADYBRy5CEyRp5Ow57AAkSZI0vxbjtsQbVm/nlEW+/bG0M60n0WeBpwJvA74KPFBV21uVLcCK9ngFcCdAVW1P8iDwhFZ+Xc9me9eRJPUwoSRJkiRp5FXVd4EjkuwPfAh4er9q7XemWTZd+Q6SrAfWA4yNjTExMTGbkOfFtm3bhrr/6WxYvb1v+di+0y+bi4V6DZbq6zudUY53If4udmY2r9NcX9/FbuNC/z2YUJIkSZK0bFTVA0kmgKOB/ZPs2XopHQJsbdW2AIcCW5LsCTweuK+nfFLvOr372AhsBFizZk2Nj48vTGNmYGJigmHufzrT9WDcsHo75948/19DN584Pu/bhKX7+k5nlONd7F6vs/mbmevru9htvHDtfgv69+AcSpIkSZJGWpIntp5JJNkX+DngVuDjwItbtZOBy9vjK9pz2vKPVVW18uPbXeAOA1YBn1mcVkjSaLGHkiRJkqRRdzBwUZtH6VHApVX14SRfAi5J8kbg88D5rf75wHuTbKLrmXQ8QFXdkuRS4EvAduC0NpROkjSFCSVJkiRJI62qvgA8q0/57fS5S1tV/TPwkmm2dTZw9nzHKEnLjQklSZI0VItxR7KpNp/zgkXfpyRJ0nLiHEqSJEmSJEkaiAklSZIkSZIkDcQhb5IkSZIkabcymyH3G1Zv55QhDNVfquyhJEmSJEmSpIHsMqGU5IIk9yb5Yk/Z65LcleSm9nNcz7Izk2xK8pUkz+8pX9vKNiU5o6f8sCTXJ7ktyQeT7D2fDZQkSZIkSdL8mkkPpQuBtX3Kz6uqI9rPVQBJDgeOB57R1nl7kj2S7AG8DTgWOBw4odUF+MO2rVXA/cCpc2mQJEmSJEmSFtYuE0pV9Qngvhlubx1wSVU9XFV3AJuAI9vPpqq6vaq+A1wCrEsS4LnAZW39i4AXDtgGSZIkSZIkLaK5TMp9epKTgBuBDVV1P7ACuK6nzpZWBnDnlPKjgCcAD1TV9j71HyHJemA9wNjYGBMTEwMHPbZvN5HWYplNjHOxbdu2Rd/nYlvubbR9o293aKMkSZKk3dtsE0rvAN4AVPt9LvBrQPrULfr3hKqd1O+rqjYCGwHWrFlT4+PjAwUN8Jb3Xc65Ny/eze02nzi+aPuCLoE1m9dllCz3Ntq+0bc7tFGSJEnS7m1WmZWqumfycZJ3Ax9uT7cAh/ZUPQTY2h73K/86sH+SPVsvpd76kiRJkiRJWoJmlVBKcnBV3d2evgiYvAPcFcD7k/wJ8GRgFfAZup5Iq5IcBtxFN3H3r1RVJfk48GK6eZVOBi6fbWMkSaMnyaOBTwD70J2XLquqs9o54xLgQOBzwMuq6jtJ9gEuBn4c+Abwy1W1uW3rTLqbO3wX+O2qunqx2yNJkhbfyjOuXJDtbli9nVMWaNuD2nzOC4YdgrSDXSaUknwAGAcOSrIFOAsYT3IE3fC0zcBvAlTVLUkuBb4EbAdOq6rvtu2cDlwN7AFcUFW3tF28BrgkyRuBzwPnz1vrJEmj4GHguVW1LclewKeSfAT4Hbq7gF6S5J10iaJ3tN/3V9VTkxxPd7fQX55yp9EnA3+d5GmT5yFpmBbqi44kSdKw7DKhVFUn9CmeNulTVWcDZ/cpvwq4qk/57XR3gZMk7YaqqoBt7ele7afo7gL6K638IuB1dAmlde0xdHcJfWu7a+j37zQK3JFk8k6jn174VkiSJEm7l36TZUuStKiS7JHkJuBe4Brgq0x/F9AVtDuHtuUP0t019PvlfdaRJEmSNI8W73ZnkiRNow1LOyLJ/sCHgKf3q9Z+T3eH0BndOTTJemA9wNjYGBMTE7MJ+RG2bds2b9satg2rt++6Uo+xfQdfZ9gW+30ftddnJob5vg/7f205/b9LkjRbJpQkSUtGVT2QZAI4munvAjp5R9EtSfYEHg/cx87vNNq7j43ARoA1a9bU+Pj4vMQ+MTHBfG1r2AadfHTD6u2ce/NofaTYfOL4vGxnpu/7UpnQdT4N832fr/dvtpbT/7skSbPlkDdJ0lAleWLrmUSSfYGfA24FJu8CCjveBfSK9py2/GNtHqYrgOOT7NPuEDd5p1FJkiRJ82y0LidKkpajg4GLkuxBd6Hj0qr6cJIv0f8uoOcD722Tbt9Hd2e3nd5pVJIkSdL8MqEkSRqqqvoC8Kw+5X3vAlpV/wy8ZJpt9b3TqDTVynkagrZh9fZlOZxNGiUuMJr1AAAgAElEQVRJDgUuBn4Y+B6wsarelOR1wG8A/9iqvrbdeZokZwKnAt8Ffruqrm7la4E3AXsA76mqcxazLZI0SkwoSZIkSRpl24ENVfW5JI8FPpvkmrbsvKr6497KSQ6n6936DODJwF8neVpb/DbgP9DNy3dDkiuq6kuL0gpJGjEmlCRJkiSNrKq6G7i7PX4oya3Aip2ssg64pKoeBu5oQ6gne8Ruaj1kSXJJq2tCSZL6MKEkSZIkaVlIspJuGPX1wHOA05OcBNxI14vpfrpk03U9q23hBwmoO6eUHzXNftYD6wHGxsaYmJiYtzYMatu2bUPd/3Q2rN7et3xs3+mXLUVLKd6ZvM9L9e9hOr3xLpXXeWeW0t/DTCz034MJJUmSJEkjL8ljgL8AXlVV30zyDuANQLXf5wK/BqTP6kX/O2BXv31V1UZgI8CaNWtqfHx8zvHP1sTEBMPc/3Smm19uw+rtnHvz6HwNXUrxbj5xfJd1lurfw3R64x2FOQmX0t/DTFy4dr8F/XsYnVdCkiRJkvpIshddMul9VfWXAFV1T8/ydwMfbk+3AIf2rH4IsLU9nq5ckjRFvyy8JEmSJI2EJAHOB26tqj/pKT+4p9qLgC+2x1cAxyfZJ8lhwCrgM8ANwKokhyXZm27i7isWow2SNIrsoSRJkiRplD0HeBlwc5KbWtlrgROSHEE3bG0z8JsAVXVLkkvpJtveDpxWVd8FSHI6cDWwB3BBVd2ymA2RpFFiQkmSJEnSyKqqT9F/XqSrdrLO2cDZfcqv2tl6kqQfMKEkSZIkSZJ2sHIRJsnesHr7SEzGrf6cQ0mSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSZIkSZI0EBNKkiRJkiRJGsieww5AkiRJkiTt3MozrtxlnQ2rt3PKDOpJ88EeSpIkSZIkSRqICSVJkiRJkiQNxISSJEmSJEmSBmJCSZIkSZIkSQMxoSRJkiRJkqSBmFCSJEmSJEnSQEwoSZIkSZIkaSAmlCRJkiRJkjQQE0qSJEmSJEkaiAklSZIkSZIkDcSEkiRJkqSRleTQJB9PcmuSW5K8spUfmOSaJLe13we08iR5c5JNSb6Q5Nk92zq51b8tycnDapMkjQITSpIkSZJG2XZgQ1U9HTgaOC3J4cAZwLVVtQq4tj0HOBZY1X7WA++ALgEFnAUcBRwJnDWZhJIkPZIJJUmSJEkjq6rurqrPtccPAbcCK4B1wEWt2kXAC9vjdcDF1bkO2D/JwcDzgWuq6r6quh+4Bli7iE2RpJGy57ADkCRJkqT5kGQl8CzgemCsqu6GLumU5Emt2grgzp7VtrSy6cr77Wc9Xe8mxsbGmJiYmLc2DGrbtm1D3f90Nqze3rd8bN/ply1FxruwjHdhLfTxwYSSJEmSpJGX5DHAXwCvqqpvJpm2ap+y2kn5IwurNgIbAdasWVPj4+MDxztfJiYmGOb+p3PKGVf2Ld+wejvn3jw6X0ONd2EZ78K6cO1+C3p8cMibJEmSpJGWZC+6ZNL7quovW/E9bSgb7fe9rXwLcGjP6ocAW3dSLknqw4SSJEmSpJGVrivS+cCtVfUnPYuuACbv1HYycHlP+Untbm9HAw+2oXFXA8ckOaBNxn1MK5Mk9TE6fbUkSZIk6ZGeA7wMuDnJTa3stcA5wKVJTgW+BrykLbsKOA7YBHwbeDlAVd2X5A3ADa3e66vqvsVpgiSNHhNKkiRJkkZWVX2K/vMfATyvT/0CTptmWxcAF8xfdJK0fM1oyFuSC5Lcm+SLPWUHJrkmyW3t9wGtPEnenGRTki8keXbPOie3+rclObmn/MeT3NzWeXN2MoOeJEmSJEmShmumcyhdCKydUnYGcG1VrQKubc8BjgVWtZ/1wDugS0ABZwFHAUcCZ00moVqd9T3rTd2XJEmSJEmSlogZJZSq6hPA1PHD64CL2uOLgBf2lF9cneuA/dtdFZ4PXFNV91XV/cA1wNq27HFV9enW/fTinm1JkiRJkiRpiZnLHEpj7W4IVNXdSZ7UylcAd/bU29LKdla+pU/5IyRZT9eTibGxMSYmJgYPel/YsHr7wOvN1mxinItt27Yt+j4X23Jvo+0bfbtDGyVJkiTt3hZiUu5+8x/VLMofWVi1EdgIsGbNmhofHx84uLe873LOvXnx5iLffOL4ou0LugTWbF6XUbLc22j7Rt/u0Mb5kuRQup6pPwx8D9hYVW9qw6Q/CKwENgMvrar72xx7b6K7O8+3gVOq6nNtWycDv9c2/caqughJkiRJC2Kmcyj1c08brkb7fW8r3wIc2lPvEGDrLsoP6VMuSVr+tgMbqurpwNHAaUkOZ37n6ZMkSZI0z+aSULoCmLxT28nA5T3lJ7W7vR0NPNiGxl0NHJPkgPYh/xjg6rbsoSRHtyvPJ/VsS5K0jFXV3ZM9jKrqIeBWumHP8zJP3yI2RZIkSdqtzGjsV5IPAOPAQUm20F0FPge4NMmpwNeAl7TqV9ENRdhENxzh5QBVdV+SNwA3tHqvr6rJib5/i+5OcvsCH2k/kqTdSJKVwLOA65m/efr67WfO8/H1s5zmzhp0rsHFnp9wKbHtw2n7sP/XltP/uyRJszWjhFJVnTDNouf1qVvAadNs5wLggj7lNwLPnEkskqTlJ8ljgL8AXlVV3+w6rPav2qds0efj62c5zZ11yhlXDlR/w+rtizo/4VJi24fT9sWeo3Kq5fT/LknSbM1lyJskSXOWZC+6ZNL7quovW/F8zdMnSZIkaQGYUJIkDU2bO+984Naq+pOeRfMyT9+iNEKSJEnaDe2efbQlSUvFc4CXATcnuamVvZb5nadPkiRJ0jwzoSRJGpqq+hT95z+CeZqnT5IkSdL8M6EkSdISt3LASbIlSZKkheYcSpIkSZIkSRqICSVJkiRJkiQNxISSJEmSJEmSBmJCSZIkSZIkSQMxoSRJkiRppCW5IMm9Sb7YU/a6JHcluan9HNez7Mwkm5J8Jcnze8rXtrJNSc5Y7HZI0igxoSRJkiRp1F0IrO1Tfl5VHdF+rgJIcjhwPPCMts7bk+yRZA/gbcCxwOHACa2uJKmPPYcdgCRJkiTNRVV9IsnKGVZfB1xSVQ8DdyTZBBzZlm2qqtsBklzS6n5pnsOVpGXBhJIkSZKk5er0JCcBNwIbqup+YAVwXU+dLa0M4M4p5Uf122iS9cB6gLGxMSYmJuY57Jnbtm3bjPZ/810PLnwwPTas7l8+ti9sWL19UWOZC+NdWMa7sGZ6fJgtE0qSJEmSlqN3AG8Aqv0+F/g1IH3qFv2nA6l+G66qjcBGgDVr1tT4+Pg8hDs7ExMTzGT/p5xx5cIHMwMbVm/n3JtH52uo8S4s411YF67db0bHh9kanVdCkiRJkmaoqu6ZfJzk3cCH29MtwKE9VQ8BtrbH05VLkqZwUm5JkiRJy06Sg3uevgiYvAPcFcDxSfZJchiwCvgMcAOwKslhSfamm7j7isWMWZJGiT2UJEmSJI20JB8AxoGDkmwBzgLGkxxBN2xtM/CbAFV1S5JL6Sbb3g6cVlXfbds5Hbga2AO4oKpuWeSmSNLIMKEkSZIkaaRV1Ql9is/fSf2zgbP7lF8FXDWPoUnSsuWQN0mSJEmSJA3EhJIkSZIkSZIGYkJJkiRJkiRJAzGhJEmSJEmSpIGYUJIkSZIkSdJATChJkiRJkiRpICaUJEmSJEmSNJA9hx2AJEmSNIiVZ1y56PvcfM4LFn2fkiQtZfZQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSZIkSZI0EBNKkiRJkiRJGogJJUmSJEmSJA3EhJIkSZIkSZIGYkJJkiRJkiRJAzGhJEmSJEmSpIGYUJIkSZIkSdJATChJkiRJkiRpICaUJEmSJI20JBckuTfJF3vKDkxyTZLb2u8DWnmSvDnJpiRfSPLsnnVObvVvS3LyMNoiSaPChJIkSZKkUXchsHZK2RnAtVW1Cri2PQc4FljVftYD74AuAQWcBRwFHAmcNZmEkiQ9kgklSZIkSSOtqj4B3DeleB1wUXt8EfDCnvKLq3MdsH+Sg4HnA9dU1X1VdT9wDY9MUkmSmj2HHYAkSZIkLYCxqroboKruTvKkVr4CuLOn3pZWNl35IyRZT9e7ibGxMSYmJuY38gFs27ZtRvvfsHr7wgczA2P7Lp1YZsJ4F5bxLqyZHh9ma84JpSSbgYeA7wLbq2pN6y76QWAlsBl4aVXdnyTAm4DjgG8Dp1TV59p2TgZ+r232jVV1EZIkSZI0v9KnrHZS/sjCqo3ARoA1a9bU+Pj4vAU3qImJCWay/1POuHLhg5mBDau3c+7No9OvwXgXlvEurAvX7jej48NszdeQt5+tqiOqak177nhlSZIkScN0TxvKRvt9byvfAhzaU+8QYOtOyiVJfSzUHEqOV5YkzYh35pEkLZArgMnzwcnA5T3lJ7VzytHAg21o3NXAMUkOaOedY1qZJKmP+eirVcBHkxTwrtb9c0HGK8/HWOXFHvO42OOpF3qM5FKw3Nto+0bf7tDGeXYh8Fbg4p6yyZ6u5yQ5oz1/DTv2dD2KrqfrUT09XdfQnZc+m+SKdpFCkrTMJfkAMA4clGQL3TnhHODSJKcCXwNe0qpfRTcFxya6aTheDlBV9yV5A3BDq/f6qpo60bckqZmPhNJzqmprSxpdk+TLO6k7p/HK8zFW+S3vu3xRxzxuPnF80fYFMx9DPcqWextt3+jbHdo4n6rqE0lWTileR/fFALqerhN0CaXv93QFrksy2dN1nNbTFSDJZE/XDyxw+JKkJaCqTphm0fP61C3gtGm2cwFwwTyGJknL1pwzK1W1tf2+N8mH6OZAuifJwa130kzHK49PKZ+Ya2ySpJE1cnfmWcieaUv9biKjdseT+WTbd5+29/5/2xNVkqQ5JpSS7Ac8qqoeao+PAV7PD8Yrn8MjxyufnuQSuqEKD7YvClcD/6NnIu5jgDPnEpskaVlasnfmWcieaUvlzjzTGbU7nswn2777tL2317k9USVJmnsPpTHgQ0kmt/X+qvrfSW7A8cqSpNmzp6skSZK0hM0poVRVtwM/1qf8GzheWZI0e/Z0lSRJkpaw3aefsiRpSfLOPJIkSdLoMaEkSRoq78wjSZIkjZ5HDTsASZIkSZIkjRYTSpIkSZIkSRqICSVJkiRJkiQNxISSJEmSJEmSBmJCSZIkSZIkSQPxLm+Slr2VZ1y5qPu7cO1+i7o/SZIkSVps9lCSJEmSJEnSQEwoSZIkSZIkaSAmlCRJkiRJkjQQE0qSJEmSJEkaiJNyS5IkSdIim6+bhmxYvZ1TFvkGJJIE9lCSJEmSJEnSgEwoSZIkSVq2kmxOcnOSm5Lc2MoOTHJNktva7wNaeZK8OcmmJF9I8uzhRi9JS5cJJUmSJEnL3c9W1RFVtaY9PwO4tqpWAde25wDHAqvaz3rgHYseqSSNCBNKkiRJknY364CL2uOLgBf2lF9cneuA/ZMcPIwAJWmpc1JuSZIkSctZAR9NUsC7qmojMFZVdwNU1d1JntTqrgDu7Fl3Syu7u3eDSdbT9WBibGyMiYmJgYPasHr7wOv0M7bv/G1rMRjvwjLehTVq8W7btm1Wx6eZMqEkSZIkaTl7TlVtbUmja5J8eSd106esHlHQJaU2AqxZs6bGx8cHDmq+7sy2YfV2zr15dL7WGe/CMt6FNWrxXrh2P2ZzfJqp0XklJElaIvrd6tnbNkvS0lRVW9vve5N8CDgSuCfJwa130sHAva36FuDQntUPAbYuasCSNCKcQ0mSJEnSspRkvySPnXwMHAN8EbgCOLlVOxm4vD2+Ajip3e3taODByaFxkqQd2UNJkiRJ0nI1BnwoCXTffd5fVf87yQ3ApUlOBb4GvKTVvwo4DtgEfBt4+eKHLEmjwYSSJEmSpGWpqm4HfqxP+TeA5/UpL+C0RQhNkkaeQ94kSZIkSZI0EHsoSZIkSbvQOxn/YkzCv/mcFyzo9iVJmit7KEmSJEmSJGkgJpQkSZIkSZI0EBNKkiRJkiRJGogJJUmSJEmSJA3EhJIkSZIkSZIGYkJJkiRJkiRJAzGhJEmSJEmSpIGYUJIkSZIkSdJATChJkiRJkiRpICaUJEmSJEmSNBATSpIkSZIkSRqICSVJkiRJkiQNxISSJEmSJEmSBmJCSZIkSZIkSQMxoSRJkiRJkqSBmFCSJEmSJEnSQJZMQinJ2iRfSbIpyRnDjkeSNHo8l0iS5spziSTNzJJIKCXZA3gbcCxwOHBCksOHG5UkaZR4LpEkzZXnEkmauSWRUAKOBDZV1e1V9R3gEmDdkGOSJI0WzyWSpLnyXCJJM5SqGnYMJHkxsLaqfr09fxlwVFWdPqXeemB9e/qvga/MYncHAV+fQ7hL3XJvHyz/Ntq+0TfbNj6lqp4438HsLhb5XNLP7vC3PR3bvnuy7UuT55I5WALnktlYyn+P/RjvwjLehbW7xDujc8mes9jwQkifskdkuqpqI7BxTjtKbqyqNXPZxlK23NsHy7+Ntm/07Q5tXKIW7VzSd+e78ftu22377mZ3bvtuYKjnktkYtb9H411YxruwjHdHS2XI2xbg0J7nhwBbhxSLJGk0eS6RJM2V5xJJmqGlklC6AViV5LAkewPHA1cMOSZJ0mjxXCJJmivPJZI0Q0tiyFtVbU9yOnA1sAdwQVXdskC7WxJdUxfQcm8fLP822r7Rtzu0cclZ5HNJP7vz+27bd0+2XcvOEjiXzMao/T0a78Iy3oVlvD2WxKTckiRJkiRJGh1LZcibJEmSJEmSRoQJJUmSJEmSJA1k2SaUkqxN8pUkm5Kc0Wf5Pkk+2JZfn2Tl4kc5ezNo3+8k+VKSLyS5NslThhHnbO2qfT31XpykkozMrRsnzaSNSV7a3sdbkrx/sWOcixn8jf5Iko8n+Xz7Oz1uGHHOVpILktyb5IvTLE+SN7f2fyHJsxc7Rs2vfu95kgOTXJPktvb7gFa+bN7/adr9uiR3Jbmp/RzXs+zM1u6vJHn+cKKeH0kObcepW9tx+JWtfHd436dr+7J/75M8Oslnkvxda/vvt/LD2mfG29pnyL1b+Uh/ptRoS7JH+yz14WHHsitJNie5uR07bhx2PLuSZP8klyX5cjsW/rthxzSdJP+657h8U5JvJnnVsOPamST/pR1jv5jkA0kePeyYdibJK1ustyzV13aQz6rzpqqW3Q/dBHpfBX4U2Bv4O+DwKXX+E/DO9vh44IPDjnue2/ezwA+1x7+13NrX6j0W+ARwHbBm2HEvwHu4Cvg8cEB7/qRhxz3P7dsI/FZ7fDiwedhxD9jGnwaeDXxxmuXHAR8BAhwNXD/smP2Z//cc+CPgjPb4DOAPl9v7P027Xwf8bp+6h7f/932Aw9pxYI9ht2EObT8YeHZ7/Fjg/7Y27g7v+3RtX/bvfXv/HtMe7wVc397PS4HjW/k7e85hI/uZ0p/R/wF+B3g/8OFhxzKDWDcDBw07jgHivQj49fZ4b2D/Ycc0w7j3AP4BeMqwY9lJjCuAO4B92/NLgVOGHddO4n0m8EXgh+hubPbXwKphx9Unzhl/Vp2vn+XaQ+lIYFNV3V5V3wEuAdZNqbOO7iABcBnwvCRZxBjnYpftq6qPV9W329PrgEMWOca5mMn7B/AGun+Qf17M4ObJTNr4G8Dbqup+gKq6d5FjnIuZtK+Ax7XHjwe2LmJ8c1ZVnwDu20mVdcDF1bkO2D/JwYsTnRbCNO9577nkIuCFPeXL4v2fwd96r3XAJVX1cFXdAWyiOx6MpKq6u6o+1x4/BNxK9yF4d3jfp2v7dJbNe9/ev23t6V7tp4Dn0n1mhEe+76P6mVIjLMkhwAuA9ww7luUmyePovpyfD1BV36mqB4Yb1Yw9D/hqVf39sAPZhT2BfZPsSZeoWcrfBZ4OXFdV366q7cDfAC8ackyPMOBn1XmxXBNKK4A7e55v4ZEfgr5fp/1RPAg8YVGim7uZtK/XqXRXTEfFLtuX5FnAoVW15Lv3TmMm7+HTgKcl+dsk1yVZu2jRzd1M2vc64FeTbAGuAv7z4oS2aAb9P9VoGququ6H7Ag48qZXvDu//6W1Y1wU93aeXbbvbMKZn0fVW2a3e9ylth93gvW/DiG4C7gWuoetx9UD7zAg7tm+UP1NqtP0p8Grge8MOZIYK+GiSzyZZP+xgduFHgX8E/qwNKXxPkv2GHdQMHQ98YNhB7ExV3QX8MfA14G7gwar66HCj2qkvAj+d5AlJfoiuR/KhQ45ppqb7zDIvlmtCqd9VoZpFnaVqxrEn+VVgDfD/L2hE82un7UvyKOA8YMOiRTT/ZvIe7kk37G0cOAF4T5L9Fziu+TKT9p0AXFhVh9AdlN/b3tvlYpSPMZq75f7+vwP4V8ARdB8Ez23ly7LdSR4D/4+9ew+3s6zv/P/+DHigeABEdhGwwZp2qjJSzQAzXnV2pUJQx9D+tAPDSLBMYx3sYX6ZKWD9FUdkijOlDliLjZIhtChSlSajKKbUPdaOIActB9EhYgoRCpZwiig19Pv747m3LMLe2WvtrOzj+3Vd61rP+j738zz3vXeynrW/6z7wSeC3qurhnRWdIDav2z9B2xfF776qHq+qw+l6eB9B9+30U4q15wXVds0PSd4A3FdVN8x2XQbwqqp6BXAccFqSV892hXZiT7qhQxdW1c8C36MbLjSntbnd3gj82WzXZWfalxEr6IZIvwDYu/3dOidV1W3A++i+YPgc3RDv7Ts9aJFYSH+89drCkzOGB/PULnQ/KtO62T2X/rv0z7Z+2keSXwB+B3hjVT02Q3Ubhqna92y6caxjSTbTzWuwIfNrYu5+/42ur6oftuED36RLMM0H/bTvVLrx0lTVl4FnAvvPSO1mRl//TzXv3Ts+pKk9jw9NXdC//6q6t/3B/Y/Ah3liaNOCa3eSp9ElVC6tqk+18KL4vU/U9sX0uwdoQ1zG6D5r7NM+M8KT2zefP1Nq/noV8Mb2Wfgy4DVJ/nR2q7RzVXV3e74PuIK5PSx2C7ClqsZ7Zn6CLsE01x0H3FhV9852RabwC8C3q+q7VfVD4FPAv5zlOu1UVV1UVa+oqlfTvcffPtt16tNkn1mGYqEmlK4DlrbVOJ5O1+1vww5lNgAr2/abgL+sNlPVPDBl+9qQsD+mSybNp7l3YIr2VdVDVbV/VS2pqiV0c0S9sarm/GoRPfr5N/rndJOrk2R/uiFwd8xoLaevn/bdSTfGmyQ/Q5dQ+u6M1nL32gCcnM5RdF1575ntSmnoeu8lK4H1PfEF+/vfYV6gX6TrCg5du09oq14dSpcE/8pM129Y2jw4FwG3VdUf9Oxa8L/3ydq+GH73SZ4/3iM4yV50f/jcBnyB7jMjPPX3Pl8/U2qeqqozq+rg9ln4BLp/d3O2h0eSvZM8e3wbOIYn3j/mnKr6O+CuJD/dQkcDX5/FKvXrROb4cLfmTuCoJD/W7jdH073PzllJDmjPLwR+ifnxc4bJP7MMxZ5TF5l/qmp7kncAV9HNcr+2qm5N8h7g+qraQPch6U+SbKLLMJ4wezUeTJ/t++/As4A/a/NC3llVb5y1Sg+gz/bNa3228SrgmCRfBx4H/nNV3T97te5fn+1bDXw4yX+kGxpwynz6AJ7kY3TDEfdv80CdRTdxK1X1Ibp5oV5HNzHto8BbZ6emGpZJfufnApcnOZXuw9GbW/EF8/ufpN2jSQ6n+7+7GXgbQPt/fjndh+7twGlV9fhs1HtIXgW8Bbi5zacD8E4Wwe+dydt+4iL43R8IrEuyB92Xr5dX1afb/fiyJO+lW4X1olZ+3n6mlGbQCHBF+7tkT+CjVfW52a3SlH4duLR9OXoHc/w9vc3t81ra+/JcVlXXJvkEcCPdPeOrdCtAz2WfTPI84Id097gHZrtCOxrws+pwrjmP/n6TJEmSJEnSHLBQh7xJkiRJkiRpNzGhJEmSJEmSpIGYUJIkSZIkSdJATChJkiRJkiRpICaUJEmSJEmSNBATSpIkSZIkSRqICSVJkiRJkiQNxISSJEmSJEmSBmJCSZIkSZIkSQMxoSRJkiRJkqSBmFCSJEmSJEnSQEwoSZIkSZIkaSAmlCRJkiRJkjQQE0qSJEmSJEkaiAklSZIkSZIkDcSEkiRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSZIkSZI0EBNKkiRJkiRJGogJJUmSJEmSJA3EhJIkSZIkSZIGYkJJkiRJkiRJAzGhJEmSJEmSpIGYUJIkSZIkSdJATChJkiRJkiRpICaUJEmSJEmSNBATSpIkSZIkSRqICSVJkiRJkiQNxISSJEmSJEmSBmJCSZIkSZIkSQMxoSRJkiRJkqSBmFCSJEmSJEnSQEwoSZIkSZIkaSAmlLSoJdmc5Bf6KPeLSe5Ksi3Jz85E3SRJs6ff+8Nc0+5TL5rtekjSYpPk55J8czdfo5K8eHdeQxqECSWpP78PvKOqnlVVX52vf2hIkha2dp+6Y1fOkWQsyb8fVp0kaSHaMblTVX9VVT89m3XqxyDv8e1vnu+3Lyu2Jfn87q6f5pc9Z7sC0jzxE8Cts10JSdL8kmTPqto+184lSQuN75G7zb+uqr+YrYv7e53b7KEkAUn+SZIzknwryf1JLk+yX5JnJNkG7AH8Tdv/J8ALgf/VMvW/Pbu1l6TFo31b+p+S3JTkoSQfT/LMJKck+dIOZX/07XGSi5P8UZLPtvfuv07y40n+R5IHknxjgiHN/zzJ19v+/5nkmT3nfkOSryV5MMn/SfLPdqjj6UluAr6XZNIv8FrZMye6TpLRJFvauf4O+J8t/qtJNiXZmmRDkhdM0uZnJPn9JHcmuTfJh5Ls1VN2RWvDw+3+tjzJOcDPAX/Yfk5/OPAvSZKGaLL3yV14j/wPSW5P8kiSs5P8ZJIvt/fCy5M8vaf8hOdK8sVW5G/ae8I0zToAACAASURBVOW/Ga9Pz7E/03oDPZjk1iRv7Nl3cZIPJvlMq8e1SX5ywJ/L65N8tdX7riTv7tn3zCR/2v6ueTDJdUlGhvUe3+6fjyZ5Xk/slUm+m+Rp7fWvJLmt/c6uSvITPWXPb3V+OMkNSX6uZ9+7k3yi1f9h4JQkRyS5vpW/N8kfTKfeGj4TSlLnN4DjgX8FvAB4APhgVT1WVc9qZV5eVT9ZVW8B7qTL1j+rqv7b7FRZkhatXwaWA4cC/ww4ZYDj3gXsDzwGfBm4sb3+BLDjB9STgGOBnwR+qh1LklcAa4G3Ac8D/hjYkOQZPceeCLwe2KePb1YnvE7z48B+dD1lVyV5DfB7rS0HAn8LXDbJed/Xznc48GLgIOB3WxuOAC4B/jOwD/BqYHNV/Q7wVzwxzPsdU9RdkmbCZO+T03mPXA68EjgK+G1gTTv/IcDL6N6/2dm5qurV7Vwvb++VH++9QEuq/C/g88ABwK8DlybpHRJ3IvBfgH2BTcA5A/5MvgecTPce/nrg7UmOb/tWAs9tbXoe8GvA96f5Hn9pSxR9PsnLAarq74Axup/NuH8HXFZVP2z1eCfwS8Dz2zU/1lP2Orp7037AR4E/S8+XNsAKuvvyPsClwPnA+VX1HLp/A5f3UW/NABNKUudtwO9U1Zaqegx4N/Cm7ORbZUnSrLmgqu6uqq10H9gP7/O4K6rqhqr6AXAF8IOquqSqHgc+DuzYQ+kPq+qudp1zaH9kAL8K/HFVXVtVj1fVOroE1VE71PGuqvp+H/Wa7DoA/wic1b7g+D7dHz1rq+rGdr86E/gXSZb0njBJWj3/Y1VtrapHgP8KnNCKnNrOs7Gq/rGqvlNV3+ijrpI0GyZ7n5zOe+T7qurhqroVuAX4fFXdUVUPAZ/liXtBX++3kzgKeBZwblX9Q1X9JfBpnvz+/qmq+kr70uFS+r+XAVBVY1V1c3sPv4kuYfOv2u4f0iWSXtzuUzdU1cODnL85CVhCl7D7AnBVkn3avnV0SSSS7NHa9idt39uA36uq21r7/itw+Hgvpar606q6v6q2V9V5wDOA3mTbl6vqz1vbvt/a8+Ik+1fVtqq6Zhpt0W5gQknq/ARwResS+iBwG/A4MDK71ZIkTeDverYfpfvQ3o97e7a/P8HrHc9zV8/239L1YIXunrF6/J7R7huH9Ozf8dipTHYdgO+2BNi4F7QyAFTVNuB+ut5HvZ4P/BhwQ08dP9fitPp+a4A6StJsmux9cjrvkf3eC/p9v53IC4C7quofd6h377HTvZcBkOTIJF9ovYceouuFtH/b/SfAVcBlSe5O8t/Gh6INoqr+uqq+X1WPVtXvAQ/SDZkDWA+8JN3Koq8FHqqqr7R9PwGc33P/2QqE1v4kq9twuIfa/uf21B2eeg89la5n2jfa8L03DNoW7R4mlKTOXcBxVbVPz+OZVfWdScrXTFZOkjSl79ElUIBufochnPOQnu0XAne37buAc3a4Z/xYVfV25x/kPjHZdSY6z910H9QBSLI33bfQO96v/p7uD6OX9tTxuT3DuO+iGzYwEe9xkuaayd4np/se2Y9dOdfdwCFJev/efuE06zGZjwIbgEOq6rnAh+iSNlTVD6vqv1TVS4B/CbyBbngc7Np7fPVc4wd0Q89OAt7CE72ToLvHvG2H++ReVfV/2nxJp9MNl9u3qvYBHho/70R1rKrbq+pEuuGD7wM+0X4fmmUmlKTOh4BzxrthJnl+khU7KX8v8KIZqZkkqR9/A7w0yeFtHoZ3D+GcpyU5OMl+dHNBjM+R8WHg19q3w0myd5sc9dlDvs5EPgq8tbXzGXTDCK6tqs29hdq34h8G3p/kAIAkByU5thW5qJ3n6HQLUxyU5J+2fd7jJM01/b5P9vUe2aepzrWz98pr6b7o+O0kT0syCvxrJp/zbjqeDWytqh+0efH+7fiOJD+f5LA2FO1huiFjj/dR7x9J8sIkr0ry9HSTfP9nul5Ef91T7BK6eQzfCPxpT/xDwJlJXtrO9dwkb+6p93bgu8CeSX4XeM4Udfl3SZ7f7m0PtvDjOztGM8OEktQ5ny7D//kkjwDXAEfupPzvAe9q3Tj/00xUUJI0uar6v8B7gL8Abge+tPMj+vJRuglV72iP97ZrXU83P9Ef0i3isIn+Jwbv+zoTqaqrgf8P+CRwD10voxMmKX56q9s1baWcv6DNUdGGJbwVeD/dN8P/mye+iT+fbh7BB5JcsAvtkqRh6et9csD3yJ3q41zvBta1vwd+eYdj/4EuyXIcXY/RPwJOHvJcdf8BeE/72+V3efJE1T9ON6n1w3RTefxvnkj49Pse/2zgQrr73HfoJjM/rqruHy9QVX9NN4/Vjb1Ju6q6gq4n0WXt/nML3c8CuqF4nwX+L90wwB8w9TDx5cCt6VbfPh84YYehjpolqbJXsyRJ0mxIshn491X1F0M41z+h+8b2J6rqzl09nyTNBcN8n9TwJflL4KNV9ZHZrotmnitYSZIkLQwvo/um9++mKihJ0q5K8s+BVwA7mypEC5hD3iRJknaTNgfFtkkeLxzidf4fuiWdT29DLSRJ80ySn5vsnjHXrpdkHd1Q6t+qqkd2R/009znkTZIkSZIkSQOxh5IkSZIkSZIGMm/nUNp///1ryZIlAx/3ve99j7333nv4FZojFnr7YOG30fbNf9Nt4w033PD3VfX83VAlTWIx3kus++yw7rNjMdbde8nMW4z3kn4s9PbBwm+j7Zv/dve9ZN4mlJYsWcL1118/8HFjY2OMjo4Ov0JzxEJvHyz8Ntq++W+6bUzyt8OvjXZmMd5LrPvssO6zYzHW3XvJzFuM95J+LPT2wcJvo+2b/3b3vWTKIW9JDknyhSS3Jbk1yW+2+H5JNia5vT3v2+JJckGSTUluSvKKnnOtbOVvT7KyJ/7KJDe3Yy5IkoFbLEmSJEmSpBnRzxxK24HVVfUzwFHAaUleApwBXF1VS4Gr22uA44Cl7bEKuBC6BBRwFnAkcARw1ngSqpVZ1XPc8l1vmiRJkiRJknaHKRNKVXVPVd3Yth8BbgMOAlYA61qxdcDxbXsFcEl1rgH2SXIgcCywsaq2VtUDwEZgedv3nKr6cnVLzl3Scy5JkiRJkiTNMQPNoZRkCfCzwLXASFXdA13SKckBrdhBwF09h21psZ3Ft0wQn+j6q+h6MjEyMsLY2Ngg1Qdg27Zt0zpuvljo7YOF30bbN/8thjZKkiRJWtz6TigleRbwSeC3qurhnUxzNNGOmkb8qcGqNcAagGXLltV0Jpda6BNvLfT2wcJvo+2b/xZDGyVJkiQtbv3MoUSSp9Elky6tqk+18L1tuBrt+b4W3wIc0nP4wcDdU8QPniAuSZIkScBOFwt6d5LvJPlae7yu55gz28I/30xybE98eYttSnJGT/zQJNe2RYQ+nuTpM9tKSZo/+lnlLcBFwG1V9Qc9uzYA4yu1rQTW98RPbqu9HQU81IbGXQUck2TfNhn3McBVbd8jSY5q1zq551ySJEmSBJMvFgTw/qo6vD2uBGj7TgBeSrfozx8l2SPJHsAH6RYTeglwYs953tfOtRR4ADh1phonSfNNP0PeXgW8Bbg5ydda7J3AucDlSU4F7gTe3PZdCbwO2AQ8CrwVoKq2JjkbuK6Ve09VbW3bbwcuBvYCPtsekiRJkgR087YC43O4PpJkfLGgyawALquqx4BvJ9lEt9o0wKaqugMgyWXAina+1wD/tpVZB7ybtmq1JOnJpkwoVdWXmHieI4CjJyhfwGmTnGstsHaC+PXAy6aqiyRJkiTtsFjQq4B3JDkZuJ6uF9MDdMmma3oO6138Z8fFgo4Engc8WFXbJyi/4/VdLGgKC719sPDbaPvmv93dxoFWeVsIbv7OQ5xyxmdm7Hqbz339jF1LkqT5aEmf9+XVh20f2j3c+7M0f02wWNCFwNl0C/ucDZwH/AqTL/4z0bQfM75Y0AcuXc95X/rewMdN10y/7y2GRUoWehtt3/y3u9u46BJKkiRJkuaniRYLqqp7e/Z/GPh0eznZokBMEv97YJ8ke7ZeSi4WJEk70dcqb5IkSZI0myZbLGh85enmF4Fb2vYG4IQkz0hyKLAU+ArdnK5L24puT6ebuHtDm7rjC8Cb2vG9Cw9JknZgDyVJkiRJ88FkiwWdmORwuuFpm4G3AVTVrUkuB75Ot0LcaVX1OECSd9CtQr0HsLaqbm3nOx24LMl7ga/SJbAkSRMwoSRJmlVJfhr4eE/oRcDvApe0+BK6PxB+uaoeaN9Qn0+3ouijwClVdWM710rgXe08762qdTPRBknS7reTxYKu3Mkx5wDnTBC/cqLj2spvR+wYlyQ9lUPeJEmzqqq+WVWHV9XhwCvpkkRXAGcAV1fVUuDq9hrgOLphC0vpVti5ECDJfsBZdCv1HAGclWTfmWyLJEmStFiYUJIkzSVHA9+qqr8FVgDjPYzWAce37RXAJdW5hm4C1QOBY4GNVbW1LRe9EVg+s9WXJEmSFgeHvEmS5pITgI+17ZGqugegqu5JckCLHwTc1XPMlhabLP4kSVbR9WxiZGSEsbGxgSu5bdu2aR03F8zFuq8+bHtf5Ub26r/sVGb6ZzAXf+79su6zYz7XXZK0OJhQkiTNCW2lnTcCZ05VdIJY7ST+5EDVGmANwLJly2p0dHSwitIlI6Zz3FwwF+t+yhmf6avc6sO2c97Nw/nosvmk0aGcp19z8efeL+s+O+Zz3SVJi4ND3iRJc8VxwI1VdW97fe/4UtDt+b4W3wIc0nPcwcDdO4lLkiRJGjITSpKkueJEnhjuBrABWNm2VwLre+Inp3MU8FAbGncVcEySfdtk3Me0mCRJkqQhc8ibJGnWJfkx4LXA23rC5wKXJzkVuBN4c4tfCbwO2ES3ItxbAapqa5KzgetaufdU1dYZqL4kSZK06JhQkiTNuqp6FHjeDrH76VZ927FsAadNcp61wNrdUUdJkiRJT3DImyRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSZIkSZI0kCkTSknWJrkvyS09sY8n+Vp7bE7ytRZfkuT7Pfs+1HPMK5PcnGRTkguSpMX3S7Ixye3ted/d0VBJkiRJkiQNRz89lC4GlvcGqurfVNXhVXU48EngUz27vzW+r6p+rSd+IbAKWNoe4+c8A7i6qpYCV7fXkiRJkiRJmqOmTChV1ReBrRPta72Mfhn42M7OkeRA4DlV9eWqKuAS4Pi2ewWwrm2v64lLkiRJkiRpDtpzF4//OeDeqrq9J3Zokq8CDwPvqqq/Ag4CtvSU2dJiACNVdQ9AVd2T5IDJLpZkFV0vJ0ZGRhgbGxu4wiN7werDtg983HRNp467Ytu2bTN+zZm20Nto++a/xdBGSZIkSYvbriaUTuTJvZPuAV5YVfcneSXw50leCmSCY2vQi1XVGmANwLJly2p0dHTgCn/g0vWcd/OuNrt/m08anbFrQZfAms7PZT5Z6G20ffPfYmijJEmSpMVt2pmVJHsCvwS8cjxWVY8Bj7XtG5J8C/gpuh5JB/ccfjBwd9u+N8mBrXfSgcB9062TJEmSJEmSdr9+JuWezC8A36iqHw1lS/L8JHu07RfRTb59RxvS9kiSo9q8SycD69thG4CVbXtlT1ySJEmSJElz0JQJpSQfA74M/HSSLUlObbtO4KmTcb8auCnJ3wCfAH6tqsYn9H478BFgE/At4LMtfi7w2iS3A69tryVJkiRJkjRHTTnkrapOnCR+ygSxTwKfnKT89cDLJojfDxw9VT0kSZIkSZI0N+zKkDdJkiRJkiQtQiaUJEmSJEmSNBATSpIkSZIkSRqICSVJkiRJkiQNxISSJEmSJEmSBmJCSZI0q5Lsk+QTSb6R5LYk/yLJfkk2Jrm9Pe/byibJBUk2JbkpySt6zrOylb89ycrZa5EkSZK08JlQkiTNtvOBz1XVPwVeDtwGnAFcXVVLgavba4DjgKXtsQq4ECDJfsBZwJHAEcBZ40koSZIkScNnQkmSNGuSPAd4NXARQFX9Q1U9CKwA1rVi64Dj2/YK4JLqXAPsk+RA4FhgY1VtraoHgI3A8hlsiiRJkrSomFCSJM2mFwHfBf5nkq8m+UiSvYGRqroHoD0f0MofBNzVc/yWFpssLkmSJGk32HO2KyBJWtT2BF4B/HpVXZvkfJ4Y3jaRTBCrncSfeoJkFd1wOUZGRhgbGxuowgDbtm2b1nFzwVys++rDtvdVbmSv/stOZaZ/BnPx594v6z475nPdJUmLgwklSdJs2gJsqapr2+tP0CWU7k1yYFXd04a03ddT/pCe4w8G7m7x0R3iYxNdsKrWAGsAli1bVqOjoxMV26mxsTGmc9xcMBfrfsoZn+mr3OrDtnPezcP56LL5pNGhnKdfc/Hn3i/rPjvmc90lSYuDQ94kSbOmqv4OuCvJT7fQ0cDXgQ3A+EptK4H1bXsDcHJb7e0o4KE2JO4q4Jgk+7bJuI9pMUnSApHkkCRfaCuC3prkN1t8aCuDJnllkpvbMRckmagHrCQJeyhJkmbfrwOXJnk6cAfwVrovPC5PcipwJ/DmVvZK4HXAJuDRVpaq2prkbOC6Vu49VbV15pogSZoB24HVVXVjkmcDNyTZCJxCtzLouUnOoOvpejpPXhn0SLqVQY/sWRl0Gd3w6BuSbGiLOlxINyz6Grp7znLgszPYRkmaN0woSZJmVVV9je5D/Y6OnqBsAadNcp61wNrh1k4ajpu/81DfQ/uGYfO5r5+xa0kzpfVIHV+w4ZEkt9EtwLCCJ4Y9r6Mb8nw6PSuDAtckGV8ZdJS2MihAS0otTzIGPKeqvtzil9CtMmpCSZImYEJJkiRJ0rySZAnws8C17LAyaJLprgx6UNveMT7R9Xd5gYdhLjTQDxcjGL6F3kbbN//t7jaaUJIkSZI0byR5FvBJ4Leq6uGdTHM06Mqgfa8YOowFHj5w6fqhLTTQDxcjGL6F3kbbN//t7jY6KbckSZKkeSHJ0+iSSZdW1ada+N42lI0BVgadLH7wBHFJ0gRMKEmSJEma89qKaxcBt1XVH/TsGsrKoG3fI0mOatc6uedckqQdTNnHMsla4A3AfVX1shZ7N/CrwHdbsXdW1ZVt35nAqcDjwG9U1VUtvhw4H9gD+EhVndvihwKXAfsBNwJvqap/GFYDJUma75YMcTLn1Ydtn3JyaCd0ljRHvQp4C3Bzkq+12DuBcxneyqBvBy4G9qKbjNsJuSVpEv0M2r0Y+EPgkh3i76+q3+8NJHkJcALwUuAFwF8k+am2+4PAa+m6kl7Xlub8OvC+dq7LknyILhl14TTbI0mSJGkBqqovMfE8RzCklUGr6nrgZbtQTUlaNKYc8lZVXwS2TlWuWQFcVlWPVdW36b4NOKI9NlXVHa330WXAitaV9DXAJ9rx6+iW5pQkSZIkSdIctSvLCrwjycnA9cDqqnqAblnNa3rK9C61uePSnEcCzwMerKrtE5R/CpfnnJpLH85/tm/+WwxtlCRJkrS4TTehdCFwNt0ymmcD5wG/wuRLbU7UE2qgpTnB5Tn74dKH85/tm/8WQxslSZIkLW7TyqxU1b3j20k+DHy6vZxsCU4mif89sE+SPVsvJZfmlCRJkiRJmuOmnENpIkkO7Hn5i8AtbXsDcEKSZ7TV25YCX6FbQWFpkkOTPJ1u4u4NbaK8LwBvasf3LvMpSZIkSZKkOWjKHkpJPgaMAvsn2QKcBYwmOZxueNpm4G0AVXVrksuBrwPbgdOq6vF2nncAVwF7AGur6tZ2idOBy5K8F/gqcNHQWidJkiRJkqShmzKhVFUnThCeNOlTVecA50wQvxK4coL4HXSrwEmSJEmSJGkemNaQN0mSJEmSJC1eJpQkSZIkSZI0EBNKkiRJkiRJGogJJUmSJEmSJA3EhJIkSZIkSZIGYkJJkiRJkiRJAzGhJEmSJEmSpIGYUJIkSZIkSdJATChJkmZdks1Jbk7ytSTXt9h+STYmub0979viSXJBkk1Jbkryip7zrGzlb0+ycrbaI0mSJC10JpQkSXPFz1fV4VW1rL0+A7i6qpYCV7fXAMcBS9tjFXAhdAko4CzgSOAI4KzxJJQkSZKk4TKhJEmaq1YA69r2OuD4nvgl1bkG2CfJgcCxwMaq2lpVDwAbgeUzXWlJkiRpMdhztisgSRJQwOeTFPDHVbUGGKmqewCq6p4kB7SyBwF39Ry7pcUmiz9JklV0PZsYGRlhbGxs4Mpu27ZtWsdN1+rDtg/tXCN7TX2+mWwb9N++furer5lu4zDr3o9htm+m/70Pk3WXJGn3MaEkSZoLXlVVd7ek0cYk39hJ2UwQq53EnxzoklVrAJYtW1ajo6MDV3ZsbIzpHDddp5zxmaGda/Vh2znv5p3f/jefNDq06/Wj3/b1U/d+zXQbP3Dp+qHVvR/DbN9M/3sfJusuSdLu45A3SdKsq6q72/N9wBV0cyDd24ay0Z7va8W3AIf0HH4wcPdO4pIkSZKGzISSJGlWJdk7ybPHt4FjgFuADcD4Sm0rgfVtewNwclvt7SjgoTY07irgmCT7tsm4j2kxSZIkSUPmkDdJ0mwbAa5IAt196aNV9bkk1wGXJzkVuBN4cyt/JfA6YBPwKPBWgKramuRs4LpW7j1VtXXmmiFJkiQtHiaUJEmzqqruAF4+Qfx+4OgJ4gWcNsm51gJrh11HSZIkSU/mkDdJkiRJkiQNxISSJEmSJEmSBjJlQinJ2iT3JbmlJ/bfk3wjyU1JrkiyT4svSfL9JF9rjw/1HPPKJDcn2ZTkgrTJMpLsl2Rjktvb8767o6GSJEmSJEkajn56KF0MLN8hthF4WVX9M+D/Amf27PtWVR3eHr/WE78QWAUsbY/xc54BXF1VS4Gr22tJkiRJkiTNUVMmlKrqi8DWHWKfr6rt7eU1wME7O0eSA4HnVNWX22SqlwDHt90rgHVte11PXJIkSZIkSXPQMFZ5+xXg4z2vD03yVeBh4F1V9VfAQcCWnjJbWgxgpKruAaiqe5IcMNmFkqyi6+XEyMgIY2NjA1d2ZC9Yfdj2qQsOyXTquCu2bds249ecaQu9jbZv/lsMbZQkSZK0uO1SQinJ7wDbgUtb6B7ghVV1f5JXAn+e5KVAJji8Br1eVa0B1gAsW7asRkdHB67zBy5dz3k3DyOP1p/NJ43O2LWgS2BN5+cynyz0Ntq++W8xtFGSJEnS4jbtzEqSlcAbgKPbMDaq6jHgsbZ9Q5JvAT9F1yOpd1jcwcDdbfveJAe23kkHAvdNt06SJEmSJEna/fqZlPspkiwHTgfeWFWP9sSfn2SPtv0iusm372hD2h5JclRb3e1kYH07bAOwsm2v7IlLkiRJkiRpDpqyh1KSjwGjwP5JtgBn0a3q9gxgY5cf4pq2oturgfck2Q48DvxaVY1P6P12uhXj9gI+2x4A5wKXJzkVuBN481BaJkmSJEmSpN1iyoRSVZ04QfiiScp+EvjkJPuuB142Qfx+4Oip6iFJkiRp8Uqylm7Kjfuq6mUt9m7gV4HvtmLvrKor274zgVPpvuj+jaq6qsWXA+cDewAfqapzW/xQ4DJgP+BG4C1V9Q8z0zpJmn+mNeRNkiRJkmbYxcDyCeLvr6rD22M8mfQS4ATgpe2YP0qyR5ue44PAccBLgBNbWYD3tXMtBR6gS0ZJkiZhQkmSJEnSnFdVXwS2TlmwswK4rKoeq6pvA5uAI9pjU1Xd0XofXQasaPO8vgb4RDt+HXD8UBsgSQuMCSVJkiRJ89k7ktyUZG2SfVvsIOCunjJbWmyy+POAB6tq+w5xSdIkppxDSZIkSZLmqAuBs4Fqz+cBvwJkgrLFxF+o107KTyjJKmAVwMjICGNjYwNVGmBkL1h92PapCw7JdOq4K7Zt2zbj15xpC72Ntm/+291tNKEkSZIkaV6qqnvHt5N8GPh0e7kFOKSn6MHA3W17ovjfA/sk2bP1UuotP9F11wBrAJYtW1ajo6MD1/0Dl67nvJtn7s+xzSeNzti1oEtgTefnMp8s9Dbavvlvd7fRIW+SJEmS5qUkB/a8/EXglra9ATghyTPa6m1Lga8A1wFLkxya5Ol0E3dvqKoCvgC8qR2/Elg/E22QpPnKHkqSJEmS5rwkHwNGgf2TbAHOAkaTHE43PG0z8DaAqro1yeXA14HtwGlV9Xg7zzuAq4A9gLVVdWu7xOnAZUneC3wVuGiGmiZJ85IJJUmSJElzXlWdOEF40qRPVZ0DnDNB/Ergygnid9CtAidJ6oND3iRJkiRJkjQQE0qSJEmSJEkaiAklSdKsS7JHkq8m+XR7fWiSa5PcnuTjbeJU2uSqH0+yqe1f0nOOM1v8m0mOnZ2WSJIkSYuDCSVJ0lzwm8BtPa/fB7y/qpYCDwCntvipwANV9WLg/a0cSV5Ct1LPS4HlwB8l2WOG6i5JkiQtOiaUJEmzKsnBwOuBj7TXAV4DfKIVWQcc37ZXtNe0/Ue38iuAy6rqsar6NrAJJ1aVJEmSdhtXeZMkzbb/Afw28Oz2+nnAg1W1vb3eAhzUtg8C7gKoqu1JHmrlDwKu6Tln7zFPkmQVsApgZGSEsbGxgSu8bdu2aR03XasP2z51oT6N7DX1+WaybdB/+/qpe79muo3DrHs/htm+mf73PkzWXZKk3ceEkiRp1iR5A3BfVd2QZHQ8PEHRmmLfzo55crBqDbAGYNmyZTU6OjpRsZ0aGxtjOsdN1ylnfGZo51p92HbOu3nnt//NJ40O7Xr96Ld9/dS9XzPdxg9cun5ode/HMNs30//eh8m6S5K0+5hQkiTNplcBb0zyOuCZwHPoeiztk2TP1kvpYODuVn4LcAiwJcmewHOBrT3xcb3HSJIkSRoy51CSJM2aqjqzqg6uqiV0k2r/ZVWdBHwBeFMrthJY37Y3tNe0/X9ZVdXiJ7RV4A4FlgJfmaFmSJIkSYuOPZQkyUNtUgAAIABJREFUSXPR6cBlSd4LfBW4qMUvAv4kySa6nkknAFTVrUkuB74ObAdOq6rHZ77akiRJ0uJgQkmSNCdU1Rgw1rbvYIJV2qrqB8CbJzn+HOCc3VdDSZIkSeP6GvKWZG2S+5Lc0hPbL8nGJLe3531bPEkuSLIpyU1JXtFzzMpW/vYkK3vir0xyczvmgrYEtCRJkiRJkuagfudQuhhYvkPsDODqqloKXN1eAxxHN3fFUrplmS+ELgEFnAUcSfet81njSahWZlXPcTteS5IkSZIkSXNEXwmlqvoi3VwVvVYA69r2OuD4nvgl1bmGbqWeA4FjgY1VtbWqHgA2AsvbvudU1ZfbxKqX9JxLkiRJkiRJc8yuzKE0UlX3AFTVPUkOaPGDgLt6ym1psZ3Ft0wQf4okq+h6MjEyMsLY2Njgld4LVh+2feDjpms6ddwV27Ztm/FrzrSF3kbbN/8thjZKkiRJWtx2x6TcE81/VNOIPzVYtQZYA7Bs2bIaHR0duHIfuHQ95908c3ORbz5pdMauBV0Cazo/l/lkobfR9s1/i6GNkiRJkha3fudQmsi9bbga7fm+Ft8CHNJT7mDg7iniB08QlyRJkiRJ0hy0KwmlDcD4Sm0rgfU98ZPbam9HAQ+1oXFXAcck2bdNxn0McFXb90iSo9rqbif3nEuSJEmSJElzTF9jv5J8DBgF9k+yhW61tnOBy5OcCtwJvLkVvxJ4HbAJeBR4K0BVbU1yNnBdK/eeqhqf6PvtdCvJ7QV8tj0kSZIkSZI0B/WVUKqqEyfZdfQEZQs4bZLzrAXWThC/HnhZP3WRJEmSJEnS7NqVIW+SJEmSJElahEwoSZIkSZIkaSAmlCRJkiRJkjQQE0qSJEmSJEkaiAklSZIkSZIkDcSEkiRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSZIkSZI0EBNKkiRJkiRJGogJJUnSrEryzCRfSfI3SW5N8l9a/NAk1ya5PcnHkzy9xZ/RXm9q+5f0nOvMFv9mkmNnp0WSJEnSwrfnbFdAkrToPQa8pqq2JXka8KUknwX+X+D9VXVZkg8BpwIXtucHqurFSU4A3gf8myQvAU4AXgq8APiLJD9VVY/PRqOk2bTkjM8M7VyrD9vOKVOcb/O5rx/a9SRJ0vxgDyVJ0qyqzrb28mntUcBrgE+0+Drg+La9or2m7T86SVr8sqp6rKq+DWwCjpiBJkiSJEmLjj2UJEmzLskewA3Ai4EPAt8CHqyq7a3IFuCgtn0QcBdAVW1P8hDwvBa/pue0vcf0XmsVsApgZGSEsbGxgeu7bdu2aR03XasP2z51oT6N7DX1+WaybdB/+/qpe79muo3DrPtMm4v/Zvo10/9Xh2k+1313SrIWeANwX1W9rMX2Az4OLAE2A79cVQ+0LxvOB14HPAqcUlU3tmNWAu9qp31vVa1r8VcCFwN7AVcCv1lVNSONk6R5xoSSJGnWtWFphyfZB7gC+JmJirXnTLJvsviO11oDrAFYtmxZjY6ODlzfsbExpnPcdE013GgQqw/bznk37/z2v/mk0aFdrx/9tq+fuvdrptv4gUvXD63uM20u/pvp10z/Xx2m+Vz33exi4A+BS3piZwBXV9W5Sc5or08HjgOWtseRdMOmj2wJqLOAZXT3iRuSbKiqB1qZVXRfUFwJLAc+OwPtkqR5xyFvkqQ5o6oeBMaAo4B9koz/FXswcHfb3gIcAtD2PxfY2huf4BhJ0gJQVV+ke8/v1TsUesch0pe0odXX0N1XDgSOBTZW1daWRNoILG/7nlNVX269ki7pOZckaQfT/qosyU/TdS0d9yLgd4F9gF8Fvtvi76yqK9sxZ9JNpvo48BtVdVWLL6frjroH8JGqOne69ZIkzS9Jng/8sKoeTLIX8At0E21/AXgTcBmwEljfDtnQXn+57f/LqqokG4CPJvkDukm5lwJfmdHGSJJmw0hV3QNQVfckOaDFfzREuhkfCr2z+JYJ4k8xjOHTMz0UdqaHUC6GYZsLvY22b/7b3W2cdkKpqr4JHA4/mvviO3TDFN5KtyrP7/eWn2z1nbb7g8Br6d60r2tdTr8+3bpJkuaVA4F17V7yT4DLq+rTSb4OXJbkvcBXgYta+YuAP0myie5b6hMAqurWJJcDXwe2A6e5wpskLWqDDpHua+g0DGf49EwPhZ3poamLYdjmQm+j7Zv/dncbh/UOdjTwrar6227uuwn9aPUd4NvtD4Hx1Xc2VdUdAEkua2VNKEnSIlBVNwE/O0H8DiZYpa2qfgC8eZJznQOcM+w6SpLmtHuTHNh6Jx0I3Nfikw2F3gKM7hAfa/GDJygvSZrAsBJKJwAf63n9jiQnA9cDq9vY5J2tvrNjl9MjJ7qIXUunZre9+c/2zX+LoY2SJM0h40Ohz+WpQ6Tf0b6wPhJ4qCWdrgL+a5J9W7ljgDOramuSR5IcBVwLnAx8YCYbIknzyS4nlJI8HXgjcGYLXQicTdc99GzgPOBXmLwL6UQTg9u1dJrstjf/2b75bzG0UZKk2ZDkY3S9i/ZPsoVutbZzgcuTnArcyRO9WK8EXgdsAh6lm5qDljg6G7iulXtPVY1P9P12upXk9qJb3c0V3iRpEsPIrBwH3FhV9wKMPwMk+TDw6fZyZ6vvuCqPJEmSpJ2qqhMn2XX0BGULOG2S86wF1k4Qvx542a7UUZIWi4l6Bw3qRHqGu7Vxy+N+EbilbW8ATkjyjCSH8sTqO9cBS5Mc2no7ndDKSpIkSZIkaQ7apR5KSX6MbnW2t/WE/1uSw+mGrW0e37ez1XeSvAO4CtgDWFtVt+5KvSRJkiRJkrT77FJCqaoeBZ63Q+wtOyk/4eo7VXUl3RhnSZIkSZIkzXHDGPImSZIkSZKkRcSEkiRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkge852BSRJmm9u/s5DnHLGZ2a7GpIkSdKssYeSJEmSJEmSBmJCSZIkSZIkSQMxoSRJkiRJkqSBmFCSJEmSJEnSQJyUW9KCt2SGJ0++ePneM3o9SZIkSZpp9lCSJEmSJEnSQEwoSZIkSZIkaSAmlCRJkiRJkjQQE0qSpFmT5JAkX0hyW5Jbk/xmi++XZGOS29vzvi2eJBck2ZTkpiSv6DnXylb+9iQrZ6tNkiRJ0mJgQkmSNJu2A6ur6meAo4DTkrwEOAO4uqqWAle31wDHAUvbYxVwIXQJKOAs4EjgCOCs8SSUJEmSpOEzoSRJmjVVdU9V3di2HwFuAw4CVgDrWrF1wPFtewVwSXWuAfZJciBwLLCxqrZW1QPARmD5DDZFkiRJWlT2nO0KSJIEkGQJ8LPAtcBIVd0DXdIpyQGt2EHAXT2HbWmxyeITXWcVXe8mRkZGGBsbG7iuI3vB6sO2D3zcXNBP3afzM9kV/f4sh/lzn+k2+m9mdmzbtm3O1m0q87nukqTFYZcTSkk2A48AjwPbq2pZG3rwcWAJsBn45ap6IEmA84HXAY8Cp4x/M93mu3hXO+17q2odkqRFIcmzgE8Cv1VVD3e3i4mLThCrncSfGqxaA6wBWLZsWY2Ojg5c3w9cup7zbp6f38msPmz7lHXffNLozFSmOeWMz/RVrp+692um2+i/mdkxNjbGdP6PzwXzue6SpMVhWEPefr6qDq+qZe21c19IkvqS5Gl0yaRLq+pTLXxvG8pGe76vxbcAh/QcfjBw907ikiRJknaD3TWHknNfSJKm1HquXgTcVlV/0LNrAzC+UttKYH1P/OS22ttRwENtaNxVwDFJ9m1fSBzTYpIkSZJ2g2H0vS7g80kK+OM2lGC3zH0xH+e9mOmx74thvP1Cb6PtG76Znrdkof8Oh+xVwFuAm5N8rcXeCZwLXJ7kVOBO4M1t35V0w6Y30Q2dfitAVW1NcjZwXSv3nqraOjNNkCRJkhafYSSUXlVVd7ek0cYk39hJ2V2a+2I+znsx03MKLIbx9gu9jbZv+Pqdn2VYLl6+94L+HQ5TVX2Jie8BAEdPUL6A0yY511pg7fBqJ0mSJGkyuzzkrarubs/3AVfQzYHk3BeSJEmSJEkL1C4llJLsneTZ49t0c1bcgnNfSJIkSZIkLVi7OvZrBLiiLe+8J/DRqvpckutw7gtJkiRJkqQFaZcSSlV1B/DyCeL349wXkiRJkiRJC9Iuz6EkSZIkSZKkxcWEkiRJkiRJkgZiQkmSJEmSJEkDMaEkSZIkad5LsjnJzUm+luT6FtsvycYkt7fnfVs8SS5IsinJTUle0XOela387UlWTnY9SVrsTChJkiRJWih+vqoOr6pl7fUZwNVVtRS4ur0GOA5Y2h6rgAuhS0ABZwFHAkcAZ40noSRJT2ZCSZIkSdJCtQJY17bXAcf3xC+pzjXAPkkOBI4FNlbV1qp6ANgILJ/pSkvSfLDnbFdAkiRJkoaggM8nKeCPq2oNMFJV9wBU1T1JDmhlDwLu6jl2S4tNFn+SJKvoejYxMjLC2NjYwJUd2QtWH7Z94OOmazp13BXbtm2b8WvOtIXeRts3/+3uNppQkiRJkrQQvKqq7m5Jo41JvrGTspkgVjuJPznQJavWACxbtqxGR0cHruwHLl3PeTfP3J9jm08anbFrQZfAms7PZT5Z6G20ffPf7m6jQ94kSZIkzXtVdXd7vg+4gm4OpHvbUDba832t+BbgkJ7DDwbu3klckrQDE0qSJEmS5rUkeyd59vg2cAxwC7ABGF+pbSWwvm1vAE5uq70dBTzUhsZdBRyTZN82GfcxLSZJ2oFD3iRJkiTNdyPAFUmg+xvno1X1uSTXAZcnORW4E3hzK38l8DpgE/Ao8FaAqtqa5GzgulbuPVW1deaaIUnzhwklSZIkSfNaVd0BvHyC+P3A0RPECzhtknOtBdYOu46StNA45E2SJEmSJEkDMaEkSZIkSZKkgZhQkiRJkiRJ0kBMKEmSJEmSJGkgJpQkSbMqydok9yW5pSe2X5KNSW5vz/u2eJJckGRTkpuSvKLnmJWt/O1JVk50LUmSJEnDYUJJkjTbLgaW7xA7A7i6qpYCV7fXAMcBS9tjFXAhdAko4CzgSOAI4KzxJJQkSZKk4dtzugcmOQS4BPhx4B+BNVV1fpJ3A78KfLcVfWdVXdmOORM4FXgc+I2quqrFlwPnA3sAH6mqc6dbL0nS/FJVX0yyZIfwCmC0ba8DxoDTW/ySttzzNUn2SXJgK7uxqrYCJNlIl6T62G6uvqRZsOSMz/RVbvVh2zmlz7JT2Xzu64dyHkmSFoppJ5SA7cDqqroxybOBG9oHeID3V9Xv9xZO8v+zd/9xmpX1ff9f77CoiCgoOkUgQupqg26DZgOktvlOJeKCqZhUUwxFMLRrEkhjum2Ctt9gNKSkDZrYGtM1IGhQJGjCVkgIQafWNiCiRH5pWWED6yKY8ENXI7r00z/ONenNMrM7Z+6Zue+ZeT0fj/sx97nOdc75XPfM3Oc+n/u6rnMUcArwIuC5wJ8leUFb/R7gFcB24MYkW6rq9iFikyQtbxNVdR9AVd2X5Dmt/FDg3oF621vZbOWSJEmSFsG8E0rtg/70h/1vJLmDPX94Pxm4rKoeBe5OspVuWALA1qq6CyDJZa2uCSVJ0u4yQ1ntofyJO0g20g2XY2Jigqmpqd5BTOzX9XxYjuYS+3xek2HM9bVcyNd9qdvo38zCWg1/Mzt37lzyY0qS1McwPZT+Vhuq8BLgBuBlwNlJ3gB8lq4X00N0yabrBzYb/PZ492+Vj12IuCRJy9b9SQ5pvZMOAR5o5duBwwfqHQbsaOWTu5VPzbTjqtoMbAZYv359TU5OzlRtj/7zpVdywS0LcgpdcpvW7dpr7NtOnVyaYJq5DkmaS+xztdRt9G9mYa2Gv5mpqSnm8/4kSdJSGfoMm+RpwEeBN1fV15O8F3gH3TfD7wAuAH6a2b89nmli8BXzrbLfZi28ld5G27fwlrpXwEr/HS6RLcDpwPnt55UD5We33qzHAo+0pNM1wK8PTMR9AvCWJY5ZkiRJWjWGSigl2ZcumXRpVX0MoKruH1j/PuDjbXG2b5XZQ/njLMdvlf02a+Gt9DbavoW3UBOyztXFG/Zf0b/DhZbkw3S9iw5Osp3ubm3nA5cnORO4B3hdq341cBKwFfgW8EaAqnowyTuAG1u9t09P0C1JkiRp4Q1zl7cAFwJ3VNU7B8oPmZ5IFfhx4Nb2fAvwoSTvpJuUey3wGbqeS2uTHAl8hW7i7p+ab1ySpOWlql4/y6rjZ6hbwFmz7Oci4KIFDE2SJEnSLIbpqvMy4DTgliQ3t7K3Aq9PcjTdsLVtwJsAquq2JJfTTba9Czirqh4DSHI2cA2wD3BRVd02RFySJEmSJElaRMPc5e3TzDwv0tV72OY84LwZyq/e03aSJEmSJEkaHzNNiC1JkiRJkiTNyoSSJEmSJEmSejGhJEmSJEmSpF5MKEmSJEmSJKkXE0qSJEmSJEnqxYSSJEmSJEmSejGhJEmSJEmSpF5MKEmSJEmSJKkXE0qSJEmSJEnqxYSSJEmSJEmSejGhJEmSJEmSpF5MKEmSJEmSJKkXE0qSJEmSJEnqxYSSJEmSJEmSejGhJEmSJEmSpF5MKEmSJEmSJKkXE0qSJEmSJEnqZc2oA5AkSZLG3RHnXLWkx7t4w/5LejxJkvoyoSRJkiRJkrTIVtqXE2Mz5C3JhiRfSrI1yTmjjkeStPx4LpEkDctziSTNzVgklJLsA7wHOBE4Cnh9kqNGG5UkaTnxXCJJGpbnEkmau7FIKAHHAFur6q6q+g5wGXDyiGOSJC0vnkskScPyXCJJc5SqGnUMJHktsKGq/kVbPg04tqrO3q3eRmBjW3wh8KV5HO5g4K+GCHfcrfT2wcpvo+1b/ubbxudV1bMXOpjVwnPJnBn7aBj7aKzG2D2XDMFzyYJa6e2Dld9G27f8Leq5ZFwm5c4MZU/IdFXVZmDzUAdKPltV64fZxzhb6e2Dld9G27f8rYY2jinPJXNg7KNh7KNh7JoHzyULZKW3D1Z+G23f8rfYbRyXIW/bgcMHlg8DdowoFknS8uS5RJI0LM8lkjRH45JQuhFYm+TIJE8CTgG2jDgmSdLy4rlEkjQszyWSNEdjMeStqnYlORu4BtgHuKiqblukww3VNXUZWOntg5XfRtu3/K2GNo4dzyVzZuyjYeyjYezqxXPJglrp7YOV30bbt/wtahvHYlJuSZIkSZIkLR/jMuRNkiRJkiRJy4QJJUmSJEmSJPWyYhNKSTYk+VKSrUnOmWH9k5N8pK2/IckRSx/l/M2hff86ye1JvpDkuiTPG0Wc87W39g3Ue22SSrLsbvc4lzYm+cn2e7wtyYeWOsZhzOFv9HuTfDLJ59vf6UmjiHO+klyU5IEkt86yPkne3dr/hSQvXeoYtbCSHN7+Zu9o/5O/MOqY5irJU5J8JslftNh/ddQx9ZVkn/Z+8fFRx9JHkm1Jbklyc5LPjjqePpIcmOSKJF9sf/c/POqY5iLJC9vrPf34epI3jzquuUryi+3/9NYkH07ylFHHpOF4XeJ1ybjzusTrknmrqhX3oJtA78vA9wFPAv4COGq3Oj8H/G57fgrwkVHHvcDt+8fAU9vzn11p7Wv1DgA+BVwPrB913IvwO1wLfB44qC0/Z9RxL3D7NgM/254fBWwbddw92/gjwEuBW2dZfxLwx0CA44AbRh2zj6F/54cAL23PDwD+90zvTeP4aH+HT2vP9wVuAI4bdVw92/CvgQ8BHx91LD3j3gYcPOo45hn7JcC/aM+fBBw46pjm0YZ9gK8Czxt1LHOM91DgbmC/tnw5cMao4/Ix1O/U6xKvS8b64XWJ1yXDPFZqD6VjgK1VdVdVfQe4DDh5tzon031QArgCOD5JljDGYey1fVX1yar6Vlu8HjhsiWMcxlx+fwDvAP4j8O2lDG6BzKWN/xJ4T1U9BFBVDyxxjMOYS/sKeHp7/gxgxxLGN7Sq+hTw4B6qnAx8oDrXAwcmOWRpotNiqKr7qupz7fk3gDvoLv7GXvs73NkW922PZXNXjiSHAa8Cfm/UsawWSZ5O9wH1QoCq+k5VPTzaqObleODLVfWXow6khzXAfknWAE9lmZ0f9QRel3hdMu68LvG6ZN5WakLpUODegeXtPPFD/9/WqapdwCPAs5YkuuHNpX2DzqTLSC4Xe21fkpcAh1fVshr6MGAuv8MXAC9I8j+TXJ9kw5JFN7y5tO9twD9Psh24Gvj5pQltyfT9P9Uy0oYjvISup8+y0IaM3Qw8AFxbVcsmduC3gF8C/s+oA5mHAv40yU1JNo46mB6+D/ga8P42BOD3kuw/6qDm4RTgw6MOYq6q6ivAbwL3APcBj1TVn442Kg3J65LH87pk/Hhd4nXJvK3UhNJMGf3dv4mdS51xNefYk/xzYD3wnxY1ooW1x/Yl+R7gXcCmJYto4c3ld7iGrnvpJPB64PeSHLjIcS2UubTv9cDFVXUYXTfMD7bf7UqxnN9jtAdJngZ8FHhzVX191PHMVVU9VlVH030zfEySF486prlI8mPAA1V106hjmaeXVdVLgROBs5L8yKgDmqM1dN3n31tVLwG+Ccw6d8g4SvIk4NXAH4w6lrlKchDdN8lHAs8F9m+f5bR8eV0yXdHrknHldYnXJfO2kl6kQduBwweWD+OJ3db+tk7rUvwM9txNbJzMpX0k+VHg3wGvrqpHlyi2hbC39h0AvBiYSrKNbhzolmU2Ad5c/0avrKrvVtXdwJfo3siXg7m070y6uSGoqj8HngIcvCTRLY05/Z9qeUmyL10y6dKq+tio45mPNmxpClgu3y6+DHh1e7+/DHh5kt8fbUhzV1U72s8HgD+k63q/HGwHtg/0ZLuCLsG0nJwIfK6q7h91ID38KHB3VX2tqr4LfAz4ByOOScPxugSvS8ac1yVel8zbSk0o3QisTXJk+3bqFGDLbnW2AKe3568FPlFtxqplYK/ta10v/yvdm/ZyGuMKe2lfVT1SVQdX1RFVdQTdWOxXV9VyunvOXP5G/4huEkOSHEzX1fSuJY1y/ubSvnvo5rYgyffTvXF/bUmjXFxbgDe0uyocRzds4b5RB6X5a/NZXAjcUVXvHHU8fSR59vQ3iUn2o7to/eJoo5qbqnpLVR3W3u9PoTtfL4seG0n2T3LA9HPgBGDGO7CMm6r6KnBvkhe2ouOB20cY0ny8nmU03K25BzguyVPbe87xdPO1afnyusTrknHndYnXJfO2ZiF2Mm6qaleSs4Fr6GZ1v6iqbkvyduCzVbWF7qLgg0m20n0DcMroIu5nju37T8DTgD9oc/rdU1WvHlnQPcyxfcvaHNt4DXBCktuBx4B/W1V/Pbqo526O7dsEvC/JL9J1uTxjGX14IsmH6br9HtzGW59LN9ExVfW7dOOvTwK2At8C3jiaSLWAXgacBtzS5iICeGtVXT3CmObqEOCSJPvQfZl0+TKe62E5mQD+sJ2H1wAfqqo/GW1Ivfw8cGn7AH4Xy+h9LMlTgVcAbxp1LH1U1Q1JrgA+B+yiu6vS5tFGpWF4XeJ1ybjzusTrkqGOvYxeJ0mSJEmSJI2BlTrkTZIkSZIkSYvEhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkaUkl+d4kO5PsM+pYllKSM5J8etRxSJIkLQQTShpbSf5Rki/NoV6SvD/JQ0k+s8AxvDXJ7y3kPnfb/2SS7Yu1/4HjVJLnL/ZxJGk2SbYl+VGAqrqnqp5WVY+NOi5JkiTNz5pRByBNS1LA2qraClBV/wN44Rw2/YfAK4DDquqbQxx/Evj9qjpsuqyqfn2++5MkSZIkaaWyh5JWgucB24ZJJkmSFk+SDwLfC/y3NtTtl1rPyTVt/VSSX0vyv9r6/5bkWUkuTfL1JDcmOWJgf38vybVJHkzypSQ/OYcYTkpye5JvJPlKkn/TyieTbG89Uv+q9aQ6dWC7Jyf5zST3JLk/ye8m2W+3bTcleSDJfUneOLDts5JsaW34DPB35/h6vWigffcneetALL+VZEd7/FaSJ+8Wyy8NxPKa1u7/3fb11oFjvC3JFUk+0l6TzyX5gYH15yT5clt3e5IfH1h3RpJPt9floSR3JzmxrXtdkpt2a8+mJH80l7ZLkqTlw4SSFkWSX24f2L/RPuwfn+SYJH+e5OH2Qfe/JHlSq/+ptulftIuJf7b7cLBZ9nkm8HvAD7ftfjXJQUk+nuRr7YPux5McNrCfZ6YbIrejrf+jJPsDfww8t+1nZ5Lntg/cvz+w7auT3NbaMJXk+wfWbUvyb5J8Ickj7UP6U3q+bs9N8tEW+91J/tVA+d8keeZA3Ze0i5992/JPJ7mjtemaJM/rc2xJWixVdRpwD/BPquppwOUzVDsFOA04lC7x8ufA+4FnAncA5wK09+trgQ8BzwFeD/xOkhftJYwLgTdV1QHAi4FPDKz7O8DB7dinA5uTTPeQ/Q3gBcDRwPNbnV/ZbdtntPIzgfckOaitew/wbeAQ4KfbY4+SHAAMjsz1AAAgAElEQVT8GfAnwHPbMa9rq/8dcFyL5QeAY4B/v1ssTxmI8X3APwd+EPhHwK8k+b6B+icDf0D3Gn8I+KPpcwrw5bbNM4BfBX4/ySED2x4LfInudfuPwIVJAmwBjhw8P7YYPri3tkuSpOXFhJIWXPsQfjbwQ+2D+yuBbcBjwC/Sffj8YeB44OcAqupH2uY/0ObV+Mhc9llVFwI/A/x52+5cur/r99P1XPpe4G+A/zKwuw8CTwVeRHcx8q7Wu+lEYEfbz9OqasduMbwA+DDwZuDZwNV037Y/aaDaTwIbgCOBvw+c0eN1+x7gvwF/QXcxcDzw5iSvbLH8OfBPBzb5KeCKqvpuktcAbwV+osX2P1qskrRcvL+qvlxVj9Al+L9cVX9WVbvokh4vafV+jO79//1VtauqPgd8FHjtXvb/XeCoJE+vqofadoP+/6p6tKr+O3AV8JMtQfIvgV+sqger6hvAr9Mlvwb3+/aq+m5VXQ3sBF6YbsLxfwr8SlV9s6puBS6Zw+vwY8BXq+qCqvp2VX2jqm5o605tx3qgqr5Gl+g5bbdYzquq7wKX0Z1vf7vt4zbgNrpz07SbquqKVv+ddMmo4wCq6g+qakdV/Z92Tr6TLoE17S+r6n1tHqxL6JJmE1X1KPARuiQSLdF3BPDxObRdkiQtIyaUtBgeA55M98F936ra1i4Sbqqq69sFwDbgvwL/3zD7nKliVf11VX20qr7VPvyfN32c9u3qicDPtAuK77aLh7n4Z8BVVXVt+/D9m8B+wD8YqPPu9gH8Qbrk0NFz3DfADwHPrqq3V9V3quouum+Xpy9cPkT3TTztIueUVgbwJuA/VNUd7eLr14Gj7aUkaRm5f+D538yw/LT2/HnAsa2n6MNJHqZLtPydvez/nwInAX+Z5L8n+eGBdQ/tNmz6L+l6Bz2b7guImwaO9SetfNpft/fdad9qsT6bbq7Ke3fb794cTtc7aCbP3W0f03EOxjI90fnftJ+zvY4MxlZV/wfYPr2/JG9IcvNAu19Ml6Ca9tWBbb/Vnk7v+xLgp9q56jTg8pZokiRJK4gJJS24Nqn2m4G3AQ8kuawN2XpBG3721SRfp0t6HLynfe1tnzPVTfLUJP81yV+243wKOLB9W3w48GBVPTSPpj3ug3z78H0vXW+iaV8deD59UTFXz6Mbcjd4kfRWYKKtv4JuaN9zgR8Biq4n0vS2vz2w3YNAdotNkkapFmg/9wL/vaoOHHg8rap+do8Hr7qxqk6m65n6Rzx+2N1BbSjdtO8FdgB/RZeEedHAsZ7Rhu3tzdeAXXTnncH97s29zD7X0g669/vd45yvv42t9ZI9DNjRvox4H13P4GdV1YHArXTnlb2qquuB79ANmfspHO4mSdKKZEJJi6KqPlRV/5Dug2/RzUHxXuCLdHdyezpdsmROH073sM+ZbKK7O9yx7TjTw+lC90H9mUkOnOkQewnhcR/k2zevhwNfmWsb9uJe4O7dLpIOqKqTAKrqYeBP6YbV/RTw4aqqgW3ftNu2+1XV/1qg2CRpWPcD37fXWnv3ceAFSU5Lsm97/NBuc/Y8TpInJTk1yTNaD9Ov0/V8HfSrrd4/oht29gfti4P3Ae9K8py2r0OTvHJvQbaeQh8D3ta+6DiKbn6mubTv7yR5c7pJuA9Icmxb92Hg3yd5dpKD6eZJ+v1Z97R3P5jkJ9JNjv5m4FHgemB/unPi1wDSTTT+4p77/gDdcPNdVfXpIWKUJEljyoSSFlySFyZ5ebo7z3yb7tvdx4AD6D7E70zy94Ddv02e9WJjD/ucyQFt/cNtEutzp1dU1X10c3P8TrrJu/dNMp1wuh94VpJnzLLfy4FXpZsMfF+6xNWjwEIlbT4DfD3d5OP7JdknyYuT/NBAnQ8Bb6AbuvGhgfLfBd4yPSltkmcked0CxSVJC+E/0CVDHmbv8x3Nqg1lPoFu2O8Oup6hv0E3LHpPTgO2tZ6rP0Ob46f5KvBQ29+ldMOiv9jW/TKwFbi+bftndF9azMXZdD1VvwpcTDe/3x619r0C+CdtuzuBf9xW/xrwWeALwC3A51rZfF1JN5z7IbrX5yfaUPDbgQvo5u67H1gH/M+e+/4gXRLK3kmSJK1Q+X8dHKSFkeTv09157fvpJgj9X8BGujvVbKbrUv954JPAy1uvI5L8DF3yZ79W/wHg96vqsNn2WVU7kpwB/IuB/TyXLtmynu7i4AK6hMu+VbWrJZneRTd59pOAT1bVT7RtL6K7680+wFHTcVfV9OSiP043J9OhwM3Az7WJTkmyrcXxZ235bYPbzvJaTU63cSD2C+guHp5Mdwedfz+wz/3a63JPVb1ot32dBvwSXS+qR4Brq+qn27qi6xm2dbZYJGk12v19eLWYyzlqyP1Pn69eWlV3LsYxJEnSaJlQkiRJq5YJpUVLKP1r4Meq6uWLsX9JkjR6a0YdgCRJ0kJIchuPn7R62puq6tKljmc2bZ6mP55p3Rwn/B5rrcdugNeMOBRJkrSI7KEkLbIkb6WbgHx3/6OqTlzqeCRJkiRJGpYJJUmSJEmSJPWybIe8HXzwwXXEEUeMOox5++Y3v8n+++8/6jCWnO1eXWx3PzfddNNfVdWzFyEkzWK+55Jx+ts2ltmNUzzGMrNxigXGKx7PJZKkcbdsE0pHHHEEn/3sZ0cdxrxNTU0xOTk56jCWnO1eXWx3P0n+cuGj0Z7M91wyTn/bxjK7cYrHWGY2TrHAeMXjuUSSNO6+Z9QBSJIkSZIkaXkxoSRJkiRJkqReTChJkiRJkiSpFxNKkiRJkiRJ6sWEkiRJkiRJknoxoSRJkiRJkqReTChJkiRJkiSpFxNKkiRJkiRJ6sWEkiRJkiRJknpZM+oAJI3WEedctWj73rRuF2fstv9t579q0Y4nrVR7+j+d6f9sWP6fSpIkaW/m3UMpyVOSfCbJXyS5LcmvtvKLk9yd5Ob2OLqVJ8m7k2xN8oUkLx3Y1+lJ7myP04dvliRJkiRJkhbLMD2UHgVeXlU7k+wLfDrJH7d1/7aqrtit/onA2vY4FngvcGySZwLnAuuBAm5KsqWqHhoiNkmSJEmSJC2SefdQqs7Otrhve9QeNjkZ+EDb7nrgwCSHAK8Erq2qB1sS6Vpgw3zjkiRJkiRJ0uIaag6lJPsANwHPB95TVTck+VngvCS/AlwHnFNVjwKHAvcObL69lc1WPtPxNgIbASYmJpiamhom/JHauXPnso5/vmz3+Nm0btei7Xtivyfuf1xfh4U0zr9vSZIkSVoIQyWUquox4OgkBwJ/mOTFwFuArwJPAjYDvwy8HchMu9hD+UzH29z2yfr162tycnKY8EdqamqK5Rz/fNnu8bPQk/kO2rRuFxfc8vi3mW2nTi7a8cbFOP++JUmSJGkhzHvI26CqehiYAjZU1X1tWNujwPuBY1q17cDhA5sdBuzYQ7kkSZIkSZLG0DB3eXt265lEkv2AHwW+2OZFIkmA1wC3tk22AG9od3s7Dnikqu4DrgFOSHJQkoOAE1qZJEmSJEmSxtAwQ94OAS5p8yh9D3B5VX08ySeSPJtuKNvNwM+0+lcDJwFbgW8BbwSoqgeTvAO4sdV7e1U9OERckiRJkiRJWkTzTihV1ReAl8xQ/vJZ6hdw1izrLgIumm8skpaPIxZxzqbZbDv/VUt+TEmSJElayRZkDiVJkiRJkiStHiaUJEmSJEmS1IsJJUmSJEmSJPViQkmSJEmSJEm9mFCSJEmSJElSLyaUJElLIslFSR5IcutA2TOTXJvkzvbzoFaeJO9OsjXJF5K8dGCb01v9O5OcPlD+g0luadu8O0mWtoWSJEnS6mFCSZK0VC4GNuxWdg5wXVWtBa5rywAnAmvbYyPwXugSUMC5wLHAMcC500moVmfjwHa7H0uSJEnSAjGhJElaElX1KeDB3YpPBi5pzy8BXjNQ/oHqXA8cmOQQ4JXAtVX1YFU9BFwLbGjrnl5Vf15VBXxgYF+SJEmSFtiaUQcgSVrVJqrqPoCqui/Jc1r5ocC9A/W2t7I9lW+fofwJkmyk68nExMQEU1NTvYPeuXPnvLabr03rds26bmK/Pa+fj/m2balfl70Zp3iMZWbjFAuMVzzjFIskSTMxoSRJGkczzX9U8yh/YmHVZmAzwPr162tycrJ3cFNTU8xnu/k645yrZl23ad0uLrhlYU/n206dnNd2S/267M04xWMsMxunWGC84hmnWCRJmolD3iRJo3R/G65G+/lAK98OHD5Q7zBgx17KD5uhXJIkSdIiMKEkSRqlLcD0ndpOB64cKH9Du9vbccAjbWjcNcAJSQ5qk3GfAFzT1n0jyXHt7m5vGNiXJEmSpAXmkDdJ0pJI8mFgEjg4yXa6u7WdD1ye5EzgHuB1rfrVwEnAVuBbwBsBqurBJO8Abmz13l5V0xN9/yzdneT2A/64PSRJkiQtAhNKkqQlUVWvn2XV8TPULeCsWfZzEXDRDOWfBV48TIySJEmS5sYhb5IkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXkwoSZIkSZIkqRcTSpIkSZIkSerFhJIkSZIkSZJ6MaEkSZIkSZKkXtYMs3GSpwCfAp7c9nVFVZ2b5EjgMuCZwOeA06rqO0meDHwA+EHgr4F/VlXb2r7eApwJPAb8q6q6ZpjYJGnaEedctaTHu3jD/kt6PEmSJElaasP2UHoUeHlV/QBwNLAhyXHAbwDvqqq1wEN0iSLaz4eq6vnAu1o9khwFnAK8CNgA/E6SfYaMTZIkSZIkSYtgqIRSdXa2xX3bo4CXA1e08kuA17TnJ7dl2vrjk6SVX1ZVj1bV3cBW4JhhYpMkSZIkSdLiGGrIG0DrSXQT8HzgPcCXgYeralersh04tD0/FLgXoKp2JXkEeFYrv35gt4PbSCO1EMOlNq3bxRlLPOxKkiRJkqTFMnRCqaoeA45OciDwh8D3z1St/cws62Yrf5wkG4GNABMTE0xNTc0n5LGwc+fOZR3/fC3Hdm9at2vvlfZiYr+F2c9ys1rbvRz/ziVJkiSpj6ETStOq6uEkU8BxwIFJ1rReSocBO1q17cDhwPYka4BnAA8OlE8b3GbwGJuBzQDr16+vycnJhQp/yU1NTbGc45/Wt/fOpnWPccGnvznUMbed/6qhtu9rIXoWbVq3iwtuWbB/t2Vjtbb74g37r4j/b0mSJEmazVBzKCV5duuZRJL9gB8F7gA+Cby2VTsduLI939KWaes/UVXVyk9J8uR2h7i1wGeGiU2SJEmSJEmLY9iuA4cAl7R5lL4HuLyqPp7kduCyJL8GfB64sNW/EPhgkq10PZNOAaiq25JcDtwO7ALOakPpJEmSJEmSNGaGSihV1ReAl8xQfhcz3KWtqr4NvG6WfZ0HnDdMPJIkSZIkSVp8Qw15kyRJkiRJ0upjQkmSJEmSJEm9mFCSJEmSJElSLyaUJEmSJEmS1IsJJUmSJEmSJPViQkmSJEmSJEm9mFCSJEmSJElSLyaUJEmSJEmS1IsJJUmSJEmSJPViQkmSJEmSJEm9mFCSJEmSJElSLyaUJEmSJEmS1IsJJUmSJEmSJPViQkmSJEmSJEm9mFCSJI1Ukl9McluSW5N8OMlTkhyZ5IYkdyb5SJIntbpPbstb2/ojBvbzllb+pSSvHFV7JEmSpNXAhJIkaWSSHAr8K2B9Vb0Y2Ac4BfgN4F1VtRZ4CDizbXIm8FBVPR94V6tHkqPadi8CNgC/k2SfpWyLJEmStJqYUJIkjdoaYL8ka4CnAvcBLweuaOsvAV7Tnp/clmnrj0+SVn5ZVT1aVXcDW4Fjlih+SZIkadUxoSRJGpmq+grwm8A9dImkR4CbgIeralerth04tD0/FLi3bbur1X/WYPkM20iSJElaYGtGHYAkafVKchBd76IjgYeBPwBOnKFqTW8yy7rZymc65kZgI8DExARTU1P9ggZ27tw5r+3ma9O6XbOum9hvz+vnY75tW+rXZW/GKR5jmdk4xQLjFc84xSJJ0kxMKEmSRulHgbur6msAST4G/APgwCRrWi+kw4Adrf524HBgexsi9wzgwYHyaYPbPE5VbQY2A6xfv74mJyd7Bz01NcV8tpuvM865atZ1m9bt4oJbFvZ0vu3UyXltt9Svy96MUzzGMrNxigXGK55xikWSpJk45E2SNEr3AMcleWqbC+l44Hbgk8BrW53TgSvb8y1tmbb+E1VVrfyUdhe4I4G1wGeWqA2SJEnSqmMPJUnSyFTVDUmuAD4H7AI+T9d76CrgsiS/1soubJtcCHwwyVa6nkmntP3cluRyumTULuCsqnpsSRsjSZIkrSLz7qGU5PAkn0xyR5LbkvxCK39bkq8kubk9ThrY5i1Jtib5UpJXDpRvaGVbk5wzXJMkSctJVZ1bVX+vql5cVae1O7XdVVXHVNXzq+p1VfVoq/vttvz8tv6ugf2cV1V/t6peWFV/PLoWSZIkSSvfMD2UdgGbqupzSQ4AbkpybVv3rqr6zcHKSY6i+yb5RcBzgT9L8oK2+j3AK+jmwLgxyZaqun2I2CRJkiRJkrRI5p1Qqqr76G7xTFV9I8kd7PkWzScDl7Vvme9uwxWOaeu2Tn/LnOSyVteEkmZ0xB4mp5UkSZIkSYtvQeZQSnIE8BLgBuBlwNlJ3gB8lq4X00N0yabrBzbbzv9LQN27W/mxsxxn6Fs9j4uVcivYvreqXozbWy8Htnt1WSn/35IkSZI0m6ETSkmeBnwUeHNVfT3Je4F3ANV+XgD8NJAZNi9mnsepZjrWQtzqeVyslFvB7ulW1jNZjNtbLwe2e3W5eMP+K+L/W5IkSZJmM9SVXpJ96ZJJl1bVxwCq6v6B9e8DPt4WtwOHD2x+GLCjPZ+tXJIkSZIkSWNmmLu8he72zXdU1TsHyg8ZqPbjwK3t+RbglCRPTnIksBb4DHAjsDbJkUmeRDdx95b5xiVJkiRJkqTFNUwPpZcBpwG3JLm5lb0VeH2So+mGrW0D3gRQVbcluZxusu1dwFlV9RhAkrOBa4B9gIuq6rYh4pIkSZIkSdIiGuYub59m5nmRrt7DNucB581QfvWetpMkSZIkSdL4mPeQN0mSJEmSJK1OJpQkSZIkSZLUiwklSZIkSZIk9WJCSZIkSZIkSb2YUJIkSZIkSVIvJpQkSZIkSZLUiwklSZIkSZIk9WJCSZIkSZIkSb2YUJIkSZIkSVIva0YdwFI74pyrlvR4285/1ZIeT5IkSZIkabHZQ0mSJEmSJEm9mFCSJEmSJElSLyaUJEmSJEmS1IsJJUmSJEmSJPViQkmSJEmSJEm9mFCSJEmSJElSLyaUJEmSJEmS1IsJJUmSJEmSJPViQkmSJEmSJEm9mFCSJEmSJElSLyaUJEmSJEmS1Mu8E0pJDk/yySR3JLktyS+08mcmuTbJne3nQa08Sd6dZGuSLyR56cC+Tm/170xy+vDNkiRJkiRJ0mIZpofSLmBTVX0/cBxwVpKjgHOA66pqLXBdWwY4EVjbHhuB90KXgALOBY4FjgHOnU5CSZIkSZIkafzMO6FUVfdV1efa828AdwCHAicDl7RqlwCvac9PBj5QneuBA5McArwSuLaqHqyqh4BrgQ3zjUuStLwkOTDJFUm+2Hq9/rC9XSVJkqTxtmYhdpLkCOAlwA3ARFXdB13SKclzWrVDgXsHNtveymYrn+k4G+l6NzExMcHU1FTvWDet29V7m2HMFuPOnTvnFf+46ft6Tuy39L+DcWC7V5eV8v+9hH4b+JOqem2SJwFPBd5K19v1/CTn0PV2/WUe39v1WLrerscO9HZdDxRwU5It7YsKSZIkSQts6IRSkqcBHwXeXFVfTzJr1RnKag/lTyys2gxsBli/fn1NTk72jveMc67qvc0wtp06OWP51NQU84l/3PR9PTet28UFtyxIHnNZsd2ry8Ub9l8R/99LIcnTgR8BzgCoqu8A30lyMjDZql0CTNEllP62tytwfevddEire21VPdj2O93b9cNL1RZJkiRpNRnqSi/JvnTJpEur6mOt+P4kh7TeSYcAD7Ty7cDhA5sfBuxo5ZO7lU8NE5ckadn4PuBrwPuT/ABwE/ALjHlv16Xuhbannn6L0RNwvm0bt9554xSPscxsnGKB8YpnnGKRJGkm804opeuKdCFwR1W9c2DVFuB04Pz288qB8rOTXEY3TOGRdpFwDfDrAxNxnwC8Zb5xSZKWlTXAS4Gfr6obkvw2/+9mDjMZi96uS93LdE+9QRejJ+BsvWv3Ztx6345TPMYys3GKBcYrnnGKRZKkmQxzl7eXAacBL09yc3ucRJdIekWSO4FXtGWAq4G7gK3A+4CfA2jDE94B3Ngeb58esiBJWvG2A9ur6oa2fAVdgun+1suVHr1dZyqXJEmStAjm/ZVmVX2amb8RBjh+hvoFnDXLvi4CLppvLJKk5amqvprk3iQvrKov0Z0/bm8Pe7tKkiRJY2r1zZYrSRo3Pw9c2u7wdhfwRroetJcnORO4B3hdq3s1cBJdb9dvtbpU1YNJpnu7gr1dJUmSpEVlQkmSNFJVdTOwfoZV9naVJEmSxtQwcyhJkiRJkiRpFTKhJEmSJEmSpF5MKEmSJEmSJKkX51CSJKmnW77yCGecc9Wow5AkSZJGxh5KkiRJkiRJ6sWEkiRJkiRJknoxoSRJkiRJkqReTChJkiRJkiSpFxNKkiRJkiRJ6sWEkiRJkiRJknoxoSRJkiRJkqReTChJkiRJkiSpFxNKkiRJkiRJ6sWEkiRJkiRJknoxoSRJkiRJkqReTChJkiRJkiSpFxNKkiRJkiRJ6sWEkiRJkiRJknoxoSRJkiRJkqRehkooJbkoyQNJbh0oe1uSryS5uT1OGlj3liRbk3wpySsHyje0sq1JzhkmJkmSJEmSJC2uYXsoXQxsmKH8XVV1dHtcDZDkKOAU4EVtm99Jsk+SfYD3ACcCRwGvb3UlSZIkSZI0htYMs3FVfSrJEXOsfjJwWVU9CtydZCtwTFu3taruAkhyWat7+zCxSZIkSZIkaXEMlVDag7OTvAH4LLCpqh4CDgWuH6izvZUB3Ltb+bEz7TTJRmAjwMTEBFNTU70D27RuV+9thjFbjDt37pxX/OOm7+s5sd/S/w7Gge1eXVbK/7ckSZIkzWYxEkrvBd4BVPt5AfDTQGaoW8w87K5m2nFVbQY2A6xfv74mJyd7B3fGOVf13mYY206dnLF8amqK+cQ/bvq+npvW7eKCWxYrjzm+bPfqcvGG/VfE/7ckSZIkzWbBr/Sq6v7p50neB3y8LW4HDh+oehiwoz2frVySJEmSJEljZthJuZ8gySEDiz8OTN8BbgtwSpInJzkSWAt8BrgRWJvkyCRPopu4e8tCxyVJkiRJkqSFMVQPpSQfBiaBg5NsB84FJpMcTTdsbRvwJoCqui3J5XSTbe8Czqqqx9p+zgauAfYBLqqq24aJS5IkSZIkSYtn2Lu8vX6G4gv3UP884LwZyq8Grh4mFkmStDCOmOd8g5vW7ZrXXIXbzn/VvI4nSZKk0VnwIW+SJEmSJEla2UwoSZIkSZIkqRcTSpIkSZIkSerFhJIkaeSS7JPk80k+3paPTHJDkjuTfKTdBZR2p9CPJNna1h8xsI+3tPIvJXnlaFoiSZIkrQ4mlCRJ4+AXgDsGln8DeFdVrQUeAs5s5WcCD1XV84F3tXokOQo4BXgRsAH4nST7LFHskiRJ0qpjQkmSNFJJDgNeBfxeWw7wcuCKVuUS4DXt+cltmbb++Fb/ZOCyqnq0qu4GtgLHLE0LJEmSpNVnzagDkCSter8F/BJwQFt+FvBwVe1qy9uBQ9vzQ4F7AapqV5JHWv1DgesH9jm4zeMk2QhsBJiYmGBqaqp3wBP7waZ1u/ZecQmshFjm8zuYi507dy7avvsylpmNUywwXvGMUyySJM3EhJIkaWSS/BjwQFXdlGRyuniGqrWXdXva5vGFVZuBzQDr16+vycnJmart0X++9EouuGU8TqGb1u1a9rFsO3Vy4YOhS1TN5/e7GIxlZuMUC4xXPOMUiyRJMxmPT6CSpNXqZcCrk5wEPAV4Ol2PpQOTrGm9lA4DdrT624HDge1J1gDPAB4cKJ82uI0kSZKkBeYcSpKkkamqt1TVYVV1BN2k2p+oqlOBTwKvbdVOB65sz7e0Zdr6T1RVtfJT2l3gjgTWAp9ZomZIkiRJq449lCRJ4+iXgcuS/BrweeDCVn4h8MEkW+l6Jp0CUFW3JbkcuB3YBZxVVY8tfdiSJEnS6mBCSZI0FqpqCphqz+9ihru0VdW3gdfNsv15wHmLF6EkSZKkaQ55kyRJkiRJUi8mlCRJkiRJktSLCSVJkiRJkiT1YkJJkiRJkiRJvZhQkiRJkiRJUi8mlCRJkiRJktSLCSVJkiRJkiT1YkJJkiRJkiRJvZhQkiRJkiRJUi9DJZSSXJTkgSS3DpQ9M8m1Se5sPw9q5Uny7iRbk3whyUsHtjm91b8zyenDxCRJkiRJkqTFNWwPpYuBDbuVnQNcV1VrgevaMsCJwNr22Ai8F7oEFHAucCxwDHDudBJKkiRJkiRJ42eohFJVfQp4cLfik4FL2vNLgNcMlH+gOtcDByY5BHglcG1VPVhVDwHX8sQklSRJkiRJksbEmkXY50RV3QdQVfcleU4rPxS4d6De9lY2W/kTJNlI17uJiYkJpqamege3ad2u3tsMY7YYd+7cOa/4x03f13Niv6X/HYwD2726rJT/b0mSJEmazWIklGaTGcpqD+VPLKzaDGwGWL9+fU1OTvYO4oxzruq9zTC2nTo5Y/nU1BTziX/c9H09N63bxQW3LOWf3Xiw3avLxRv2XxH/35IkSZI0m8W4y9v9bSgb7ecDrXw7cPhAvcOAHXsolyRJkiRJ0hhajITSFmD6Tm2nA1cOlL+h3e3tOOCRNjTuGuCEJAe1ybhPaGWSJEmSJEkaQ0ONRUnyYWASODjJdrq7tZ0PXJ7kTInHqPsAAAxdSURBVOAe4HWt+tXAScBW4FvAGwGq6sEk7wBubPXeXlW7T/QtSZIkSZKkMTFUQqmqXj/LquNnqFvAWbPs5yLgomFikSRJkiRJ0tJYjCFvkiRJkiRJWsFMKEmSJEmSJKkXE0qSJEmSJEnqZag5lLR3R5xz1Yzlm9bt4oxZ1g1j2/mvWvB9SpIkSZIkDbKHkiRJkiRJknqxh5IkSRqp2XrzDmtPvYHt0StJkjQcE0orzGJ9KJckSZIkSZrmkDdJkiRJkiT1YkJJkiRJkiRJvZhQkiRJkiRJUi8mlCRJkiRJktSLCSVJkiRJkiT1YkJJkjQySQ5P8skkdyS5LckvtPJnJrk2yZ3t50GtPEnenWRrki8keenAvk5v9e9Mcvqo2iRJkiStBiaUJEmjtAvYVFXfDxwHnJXkKOAc4LqqWgtc15YBTgTWtsdG4L3QJaCAc4FjgWOAc6eTUJIkSZIWngklSdLIVNV9VfW59vwbwB3AocDJwCWt2iXAa9rzk4EPVOd64MAkhwCvBK6tqger6iHgWmDDEjZFkiRJWlXWjDoASZIAkhwBvAS4AZioqvugSzoleU6rdihw78Bm21vZbOUzHWcjXe8mJiYmmJqa6h3rxH6wad2u3tstBmOZ3Z7imc/vfRg7d+5c8mPOxlhmN07xjFMskiTNxISSJGnkkjwN+Cjw5qr6epJZq85QVnsof2Jh1WZgM8D69etrcnKyd7z/+dIrueCW8TiFblq3y1hmsad4tp06uaSxTE1NMZ+/tcVgLLMbp3jGKRZJkmbikDdJ0kgl2ZcumXRpVX2sFd/fhrLRfj7QyrcDhw9sfhiwYw/lkiRJkhaBCSVJ0sik64p0IXBHVb1zYNUWYPpObacDVw6Uv6Hd7e044JE2NO4a4IQkB7XJuE9oZZIkSZIWwfj0S5ckrUYvA04Dbklycyt7K3A+cHmSM4F7gNe1dVcDJwFbgW8BbwSoqgeTvAO4sdV7e1U9uDRNkCRJklYfE0qSpJGpqk8z8/xHAMfPUL+As2bZ10XARQsXnSRJkqTZLNqQtyTbktyS5OYkn21lz0xybZI728+DWnmSvDvJ1iRfSPLSxYpLkiRJkiRJw1nsOZT+cVUdXVXr2/I5wHVVtRa4ri0DnAisbY+NwHsXOS5JkiRJkiTN01JPyn0ycEl7fgnwmoHyD1TneuDA6bv7SJIkSZIkabwsZkKpgD9NclOSja1sot2Nh/bzOa38UODegW23tzJJkiRJkiSNmcWclPtlVbUjyXOAa5N8cQ91Z5qQtZ5QqUtMbQSYmJhgamqqd1Cb1u3qvc1imNhvfGJZSrZ7dVmt7d65c+e83p8kSZIkablYtIRSVe1oPx9I8ofAMcD9SQ6pqvvakLYHWvXtwOEDmx8G7Jhhn5uBzQDr16+vycnJ3nGdcc5VvbdZDJvW7eKCW1bfTfZs9+qyWtt98Yb9mc/7kyRJkiQtF4sy5C3J/kkOmH4OnADcCmwBTm/VTgeubM+3AG9od3s7DnhkemicJEmSJEmSxstidR2YAP4wyfQxPlRVf5LkRuDyJGcC9wCva/WvBk4CtgLfAt64SHFJkiRJkiRpSIuSUKqqu4AfmKH8r4HjZygv4KzFiEWSJEmSJEkLa/VNbiJJkrTEbvnKI0s6j+O281+1ZMeSJEmr06LMoSRJkiRJkqSVy4SSJEmSJEmSejGhJEmSJEmSpF5MKEmSJEmSpP/b3r2FWlrWcRz//pitqFNhecIcSwMxxfDQMFnCUFoxpmhFgUJiUdmFloYQ1k10ZxBRFxGImkKmmAcSi1Gx01WWR3QaRTOzSXOMDlZCOvXvYr3CMM4Y77TX+zzL/f3AZh32MOv3rrV5/rN+s553S6NYKEmSJEmSJGkUCyVJkiRJkiSNYqEkSZIkSZKkUSyUJEmSJEmSNIqFkiRJkiRJkkaxUJIkSZIkSdIoFkqSJEmSJEkaxUJJkiRJkiRJo1goSZIkSZIkaRQLJUmSJEmSJI1ioSRJkiRJkqRRLJQkSZIkSZI0ioWSJEmSJEmSRllqHUCSJEnL67BLfrjL7138tm18/BW+vzueuPS0Zf37evRKz+k8XLVh9aSPJ0nSWBZKkiRJ+r/sbtmyu+XWSiiwJEnqnVveJEmSJEmSNIqFkiRJkiRJkkbpplBKsiHJI0keS3JJ6zySpMXjLJEkSZKm0UWhlGQV8C3gVOBo4OwkR7dNJUlaJM4SSZIkaTpdFErAOuCxqnq8ql4ArgPObJxJkrRYnCWSJEnSRFJVrTOQ5CPAhqr61HD7HOAdVXXBDn/uPOC84eaRwCOTBl1e+wN/ah2iAY97ZfG4x3lzVR2w3GFWiolnSU8/22bZtZ7ymGXnesoCfeVxlkiSurbUOsAgO7nvZU1XVV0GXDb/OPOX5O6qWts6x9Q87pXF49bEJpslPb3GZtm1nvKYZed6ygJ95ekpiyRJO9PLlrctwKHb3V4DPNUoiyRpMTlLJEmSpIn0Uij9CjgiyeFJ9gTOAm5pnEmStFicJZIkSdJEutjyVlXbklwA3AasAq6sqk2NY83bq2Lr3m7wuFcWj1uTmXiW9PQam2XXespjlp3rKQv0laenLJIkvUwXJ+WWJEmSJEnS4uhly5skSZIkSZIWhIWSJEmSJEmSRrFQmliSQ5P8JMnmJJuSXNg601SSrEpyX5JbW2eZSpJ9k9yQ5OHhNX9n60xTSPL54ef7oSTXJtmrdaZ5SXJlkq1JHtruvjckuSPJo8Pl61tm1PLobf1OsleSXyZ5YMjzlZZ5hkxdrPNJnkjyYJL7k9zdOEs3cyDJkcNz8tLXc0kuapinm1mR5MIhx6YWz4mzRJK0iCyUprcNuLiqjgJOBM5PcnTjTFO5ENjcOsTEvglsrKq3AseyAo4/ySHA54C1VXUMs5Mjn9U21VxdBWzY4b5LgDur6gjgzuG2Fl9v6/e/gJOr6ljgOGBDkhMb5oG+1vn3VNVxVbW2cY5u5kBVPTI8J8cBbweeB25ukaWnWZHkGODTwDpmr9HpSY6YOMZVOEskSQvGQmliVfV0Vd07XP87s39YHtI21fwlWQOcBlzeOstUkrwOWA9cAVBVL1TVX9ummswSsHeSJWAf4KnGeeamqn4O/HmHu88Erh6uXw18cNJQmove1u+a+cdwc4/hq9lv2liJ6/z/0vkcOAX4TVX9rmGGXmbFUcAvqur5qtoG/Az40JQBnCWSpEVkodRQksOA44G72iaZxDeALwD/aR1kQm8BngW+M2wBuTzJ6tah5q2q/gB8DXgSeBr4W1Xd3jbV5A6qqqdhVkIABzbOo2XWy/o9bDG7H9gK3FFVLfP0tM4XcHuSe5Kc1zBHz3PgLODaVg/e2ax4CFifZL8k+wAfAA5tlGV7zhJJUtcslBpJ8hrgRuCiqnqudZ55SnI6sLWq7mmdZWJLwAnAt6vqeOCfrICPqw/neDgTOBx4I7A6ycfappKWT0/rd1X9e9i+tAZYN2zdmVyH6/xJVXUCcCqzrYnrG+Xocg4k2RM4A/h+wwzdzIqq2gx8FbgD2Ag8wGyLqyRJegUWSg0k2YPZm5Frquqm1nkmcBJwRpIngOuAk5N8t22kSWwBtmz3iYEbmL2xeLV7L/Dbqnq2ql4EbgLe1TjT1J5JcjDAcLm1cR4tk17X72Eb1U95+TlYptLVOl9VTw2XW5mdI2hdoyi9zoFTgXur6pmGGbqaFVV1RVWdUFXrmW09e7RVlu04SyRJXbNQmliSMDuXwuaq+nrrPFOoqi9W1ZqqOozZR+x/XFWv+k+sVNUfgd8nOXK46xTg1w0jTeVJ4MQk+ww/76fQz0l6p3ILcO5w/VzgBw2zaJn0tn4nOSDJvsP1vZm9QX+4RZae1vkkq5O89qXrwPuZbWmaXMdz4GwabncbdDUrkhw4XL4J+DDtnx9wlkiSOrfUOsAKdBJwDvDgcN4LgC9V1Y8aZtL8fBa4Zthe8DjwicZ55q6q7kpyA3Avsy0D9wGXtU01P0muBd4N7J9kC/Bl4FLg+iSfZPam6aPtEmoZ9bZ+HwxcnWQVs/8gur6qbm2UpScHATfPOgqWgO9V1caGebqaA8M5gt4HfKZljg5nxY1J9gNeBM6vqr9M+eDOEknSIkpVs18II0mSJEmSpAXkljdJkiRJkiSNYqEkSZIkSZKkUSyUJEmSJEmSNIqFkiRJkiRJkkaxUJIkSZIkSdIoFkqSJEmSJEkaxUJJkiRJkiRJo/wXYOtdSnAuMMoAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x23028eff3c8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Histogram of numeric variables\n",
    "num_bins = 10\n",
    "\n",
    "hr.hist(bins=num_bins, figsize=(20,15))\n",
    "plt.savefig(\"hr_histogram_plots\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create Dummy Variable for Categorical Variable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are two categorical variables in the dataset and they need to be converted to dummy variables before they can be used for modelling."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
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
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation_rating</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>left</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "      <th>department</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.8</td>\n",
       "      <td>5.3</td>\n",
       "      <td>3</td>\n",
       "      <td>167</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>8.0</td>\n",
       "      <td>8.6</td>\n",
       "      <td>6</td>\n",
       "      <td>272</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.1</td>\n",
       "      <td>8.8</td>\n",
       "      <td>8</td>\n",
       "      <td>282</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.7</td>\n",
       "      <td>5.2</td>\n",
       "      <td>3</td>\n",
       "      <td>169</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.1</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3</td>\n",
       "      <td>163</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   satisfaction_level  last_evaluation_rating  number_project  \\\n",
       "0                 3.8                     5.3               3   \n",
       "1                 8.0                     8.6               6   \n",
       "2                 1.1                     8.8               8   \n",
       "3                 3.7                     5.2               3   \n",
       "4                 4.1                     5.0               3   \n",
       "\n",
       "   average_montly_hours  time_spend_company  Work_accident  left  \\\n",
       "0                   167                   3              0     1   \n",
       "1                   272                   6              0     1   \n",
       "2                   282                   4              0     1   \n",
       "3                   169                   3              0     1   \n",
       "4                   163                   3              0     1   \n",
       "\n",
       "   promotion_last_5years department  salary  \n",
       "0                      0      sales     low  \n",
       "1                      0      sales  medium  \n",
       "2                      0      sales  medium  \n",
       "3                      0      sales     low  \n",
       "4                      0      sales     low  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "cat_vars=['department','salary']\n",
    "for var in cat_vars:\n",
    "    cat_list='var'+'_'+var\n",
    "    cat_list = pd.get_dummies(hr[var], prefix=var)\n",
    "    hr1=hr.join(cat_list)\n",
    "    hr=hr1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We drop the actual categorical variables once the dummy variables have been created."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "hr.drop(hr.columns[[8, 9]], axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Column names after creating dummy variables for categorical variables:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['satisfaction_level', 'last_evaluation_rating', 'number_project',\n",
       "       'average_montly_hours', 'time_spend_company', 'Work_accident',\n",
       "       'left', 'promotion_last_5years', 'department_RandD',\n",
       "       'department_accounting', 'department_hr', 'department_management',\n",
       "       'department_marketing', 'department_product_mng',\n",
       "       'department_sales', 'department_technical', 'salary_high',\n",
       "       'salary_low', 'salary_medium'], dtype=object)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr.columns.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "hr_vars=hr.columns.values.tolist()\n",
    "y=['left']\n",
    "X=[i for i in hr_vars if i not in y]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The response variable is “left”, and all the other variables are predictors."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['satisfaction_level',\n",
       " 'last_evaluation_rating',\n",
       " 'number_project',\n",
       " 'average_montly_hours',\n",
       " 'time_spend_company',\n",
       " 'Work_accident',\n",
       " 'promotion_last_5years',\n",
       " 'department_RandD',\n",
       " 'department_accounting',\n",
       " 'department_hr',\n",
       " 'department_management',\n",
       " 'department_marketing',\n",
       " 'department_product_mng',\n",
       " 'department_sales',\n",
       " 'department_technical',\n",
       " 'salary_high',\n",
       " 'salary_low',\n",
       " 'salary_medium']"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feature Selection"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Recursive Feature Elimination (RFE) works by recursively removing variables and building a model on those variables that remain. It uses the model accuracy to identify which variables (and combination of variables) contribute the most to predicting the target attribute.\n",
    "\n",
    "Let’s use feature selection to help us decide which variables are significant that can predict employee turnover with great accuracy. There are total 18 columns in X, we will select 10 initially."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ True False False False  True  True  True  True False  True  True False\n",
      " False False False  True  True  True]\n",
      "[1 7 2 9 1 1 1 1 3 1 1 5 8 6 4 1 1 1]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_selection import RFE\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "#Recursive Feature Elimination (RFE)\n",
    "model = LogisticRegression()\n",
    "\n",
    "rfe = RFE(model, 10)\n",
    "rfe = rfe.fit(hr[X], hr[y])\n",
    "print(rfe.support_)\n",
    "print(rfe.ranking_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see that RFE chose the 10 variables for us, which are marked True in the support_ array and marked with a choice “1” in the ranking_array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "cols=['satisfaction_level', 'last_evaluation_rating', 'time_spend_company', 'Work_accident', 'promotion_last_5years', \n",
    "      'department_RandD', 'department_hr', 'department_management', 'salary_high', 'salary_low'] \n",
    "X=hr[cols]\n",
    "y=hr['left']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Logistic Regression Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Split data into training and test samples\n",
    "from sklearn.cross_validation import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Logistic Regression Classifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn import metrics\n",
    "logreg = LogisticRegression()\n",
    "logreg.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic regression accuracy: 0.767\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "print('Logistic regression accuracy: {:.3f}'.format(accuracy_score(y_test, logreg.predict(X_test))))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Random Forest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',\n",
       "            max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
       "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "            min_samples_leaf=1, min_samples_split=2,\n",
       "            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,\n",
       "            oob_score=False, random_state=None, verbose=0,\n",
       "            warm_start=False)"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Random Forest Classifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "rf = RandomForestClassifier()\n",
    "rf.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Forest Accuracy: 0.989\n"
     ]
    }
   ],
   "source": [
    "print('Random Forest Accuracy: {:.3f}'.format(accuracy_score(y_test, rf.predict(X_test))))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Support Vector Machine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,\n",
       "  decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',\n",
       "  max_iter=-1, probability=False, random_state=None, shrinking=True,\n",
       "  tol=0.001, verbose=False)"
      ]
     },
     "execution_count": 187,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#SVM Classifier\n",
    "from sklearn.svm import SVC\n",
    "svc = SVC()\n",
    "svc.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Support vector machine accuracy: 0.960\n"
     ]
    }
   ],
   "source": [
    "print('Support vector machine accuracy: {:.3f}'.format(accuracy_score(y_test, svc.predict(X_test))))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Out of the three models, Random Forest has the best performance. We will perform 10-fold cross validation to confirm our results."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 10 Fold Cross Validation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Cross validation attempts to avoid overfitting while still producing a prediction for each observation dataset. We are using 10-fold Cross-Validation to train our Random Forest and SVM  model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10-fold cross validation average accuracy for Random Forest Classifier: 0.988\n"
     ]
    }
   ],
   "source": [
    "#For Random Forest\n",
    "from sklearn import model_selection\n",
    "from sklearn.model_selection import cross_val_score\n",
    "kfold = model_selection.KFold(n_splits=10, random_state=7)\n",
    "modelCV = RandomForestClassifier()\n",
    "scoring = 'accuracy'\n",
    "results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)\n",
    "print(\"10-fold cross validation average accuracy for Random Forest Classifier: %.3f\" % (results.mean()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10-fold cross validation average accuracy for SVM Classifier: 0.959\n"
     ]
    }
   ],
   "source": [
    "#For SVM\n",
    "from sklearn import model_selection\n",
    "from sklearn.model_selection import cross_val_score\n",
    "kfold = model_selection.KFold(n_splits=10, random_state=7)\n",
    "modelCV = SVC()\n",
    "scoring = 'accuracy'\n",
    "results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)\n",
    "print(\"10-fold cross validation average accuracy for SVM Classifier: %.3f\" % (results.mean()))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the CV results we observe that the average accuracy remains very close to the Random Forest & SVM  model accuracy; hence, we can conclude that the models generalize well."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Precision and Recall"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We construct confusion matrix to visualize predictions made by a classifier and evaluate the accuracy of a classification."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             precision    recall  f1-score   support\n",
      "\n",
      "          0       0.99      0.99      0.99      5840\n",
      "          1       0.98      0.98      0.98      1808\n",
      "\n",
      "avg / total       0.99      0.99      0.99      7648\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Precison Recall Scores for Random Forest\n",
    "from sklearn.metrics import classification_report\n",
    "print(classification_report(y_test, rf.predict(X_test)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1830f6e7710>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Confusion Matrix for Random Forest\n",
    "y_pred = rf.predict(X_test)\n",
    "from sklearn.metrics import confusion_matrix\n",
    "import seaborn as sns\n",
    "forest_cm = metrics.confusion_matrix(y_pred, y_test, [1,0])\n",
    "sns.heatmap(forest_cm, annot=True, fmt='.2f',xticklabels = [\"Left\", \"Stayed\"] , yticklabels = [\"Left\", \"Stayed\"] )\n",
    "plt.ylabel('True class')\n",
    "plt.xlabel('Predicted class')\n",
    "plt.title('Random Forest')\n",
    "plt.savefig('random_forest')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             precision    recall  f1-score   support\n",
      "\n",
      "          0       0.80      0.92      0.86      5840\n",
      "          1       0.51      0.26      0.34      1808\n",
      "\n",
      "avg / total       0.73      0.77      0.74      7648\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#PRScores for Logistic Regression\n",
    "print(classification_report(y_test, logreg.predict(X_test)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1830262bc18>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Confusion Matrix for Logistic Regression\n",
    "logreg_y_pred = logreg.predict(X_test)\n",
    "logreg_cm = metrics.confusion_matrix(logreg_y_pred, y_test, [1,0])\n",
    "sns.heatmap(logreg_cm, annot=True, fmt='.2f',xticklabels = [\"Left\", \"Stayed\"] , yticklabels = [\"Left\", \"Stayed\"] )\n",
    "plt.ylabel('True class')\n",
    "plt.xlabel('Predicted class')\n",
    "plt.title('Logistic Regression')\n",
    "plt.savefig('logistic_regression')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             precision    recall  f1-score   support\n",
      "\n",
      "          0       0.97      0.97      0.97      5840\n",
      "          1       0.92      0.91      0.92      1808\n",
      "\n",
      "avg / total       0.96      0.96      0.96      7648\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#PR scores for SVM\n",
    "print(classification_report(y_test, svc.predict(X_test)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x183008da400>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Confusion Matrix for SVM\n",
    "svc_y_pred = svc.predict(X_test)\n",
    "svc_cm = metrics.confusion_matrix(svc_y_pred, y_test, [1,0])\n",
    "sns.heatmap(svc_cm, annot=True, fmt='.2f',xticklabels = [\"Left\", \"Stayed\"] , yticklabels = [\"Left\", \"Stayed\"] )\n",
    "plt.ylabel('True class')\n",
    "plt.xlabel('Predicted class')\n",
    "plt.title('Support Vector Machine')\n",
    "plt.savefig('support_vector_machine')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When an employee left, how often does the classifier predict that correctly? This measurement is called \"recall\" and a quick look at these diagrams can demonstrate that random forest is clearly best for this criteria. Out of all the turnover cases, random forest correctly retrieved 1764 out of 1808. This translates to a turnover \"recall\" of about 97.5% (1764/1808), far better than logistic regression (25.6%) or support vector machines (91.3%).\n",
    "\n",
    "When a classifier predicts an employee will leave, how often does that employee actually leave? This measurement is called \"precision\". Random forest again out preforms the other two at about 97.6% precision (1764 out of 1807) with logistic regression at about 51.3% (463 out of 902), and support vector machine at about 91.8% (1651 out of 1797)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## ROC Curve"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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UaKE289x8OBBVb9+/avev0ePHur7779XSim1cuVKVatWrXyJKyUlJV+Ok5+GDh2qfvrpJ5e3T01NdWM0Vzpz5oyqXr26OnPmjDp79qyqXr26Onv27BXbvf7662rixIlXLJ8yZYrq2bOnUkqpkydPqqZNm6q0tDSllFIzZ85U48aNy/K8Wf2voO82varrbqGpehry3WZi4pOITUwh1aZo5ontE1OnwquvwqVLMGYMvPKKHgrcyLMxP293VDHml3qVSvH6vfXzvN/hw4fp1asXp06donz58nz++edUrVqV/fv38/jjj5OWlsZdd93Fe++9R0JCAocOHaJz585s27aN7du389RTT5GcnIzNZmPu3LmMHDmS/fv306RJEzp27Mjzzz/v2D4tLY1XXnmFJUuWICI888wzDBgwINvYWrVqxdGjRx2vIyMjGTx4MAkJCYSGhjJz5kwqVqzIhg0b6N27NyVKlKBt27b8+uuvbNu2jZkzZ7Jw4UKSkpK4cOECK1euZOLEiXz33XdcunSJ++67jzFjxnDhwgX+85//EB0dTVpaGiNHjuThhx9m2LBhLFiwgGLFinHHHXfwzjvvMHr0aIKDgxk6dChRUVH07duXxMREatasyYwZMwgJCaF9+/a0aNGCVatWERsby2effUa7du2ueH9z585l3LhxABw6dIju3btz4cIFAKZMmULr1q1ZvXo1Y8aMoWLFikRFRbFjxw6++uorJk+eTHJyMi1atODDDz/E19eX5557jg0bNnDx4kUefPBBxowZk+e/B2dLliyhY8eOlC1bFoCOHTuyePFiHn30UZf237FjBx06dACgQoUKlClThoiICJo3b06XLl1o164dr7322jXF6IpCUc/x5q+7mLsxmt/3nmb7sTjqXBfMk63DrQ7rSpGR0KIFbN0Ko0aZJFFI9O/fnyeffJItW7bw+OOPM3DgQAAGDRrEoEGD2LBhA5UqVcpy32nTpjFo0CCioqKIiIggLCyMN998k5o1axIVFcXEiRlHtZk+fToHDx5k06ZNjvPlZPHixXTr1g3Q/VAGDBjADz/8QGRkJL169XJcZJ566immTZvG2rVr8c00ydXatWv54osvWLlyJUuXLmXv3r2sX7+eqKgoIiMjWbNmDYsXL6ZSpUps3ryZbdu2ceedd3L27FnmzZvH9u3b2bJlCyNGjLgivieffJK3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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x18302694128>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.metrics import roc_auc_score\n",
    "from sklearn.metrics import roc_curve\n",
    "\n",
    "#ROC for logistic regression\n",
    "logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))\n",
    "fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])\n",
    "\n",
    "#ROC for Random Forrest\n",
    "rf_roc_auc = roc_auc_score(y_test, rf.predict(X_test))\n",
    "rf_fpr, rf_tpr, rf_thresholds = roc_curve(y_test, rf.predict_proba(X_test)[:,1])\n",
    "\n",
    "#ROC Curve for Random Forest & Logistic Regression\n",
    "plt.figure()\n",
    "plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)\n",
    "plt.plot(rf_fpr, rf_tpr, label='Random Forest (area = %0.2f)' % rf_roc_auc)\n",
    "plt.plot([0, 1], [0, 1],'r--')\n",
    "plt.xlim([0.0, 1.0])\n",
    "plt.ylim([0.0, 1.05])\n",
    "plt.xlabel('False Positive Rate')\n",
    "plt.ylabel('True Positive Rate')\n",
    "plt.title('Receiver operating characteristic')\n",
    "plt.legend(loc=\"lower right\")\n",
    "plt.savefig('ROC')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The receiver operating characteristic (ROC) curve is another common tool used with binary classifiers. The dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Variable Imporatnce for Random Forest Classifier"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "According to our Random Forest model, the  the most important features which influence whether to leave the company, in ascending order are as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "promotion_last_5years-0.17%\n",
      "department_management-0.21%\n",
      "department_RandD-0.24%\n",
      "department_hr-0.27%\n",
      "salary_high-0.70%\n",
      "salary_low-1.00%\n",
      "Work_accident-1.57%\n",
      "last_evaluation-18.04%\n",
      "time_spend_company-27.72%\n",
      "satisfaction_level-50.08%\n"
     ]
    }
   ],
   "source": [
    "feature_labels = np.array(['satisfaction_level', 'last_evaluation', 'time_spend_company', 'Work_accident', 'promotion_last_5years', \n",
    "      'department_RandD', 'department_hr', 'department_management', 'salary_high', 'salary_low'])\n",
    "importance = rf.feature_importances_\n",
    "feature_indexes_by_importance = importance.argsort()\n",
    "for index in feature_indexes_by_importance:\n",
    "    print('{}-{:.2f}%'.format(feature_labels[index], (importance[index] *100.0)))\n",
    "    analysis_result += ('{}-{:.2f}%'.format(feature_labels[index], (importance[index] *100.0)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [],
   "source": [
    "file = open(\"variable_importance.txt\",\"w+\")\n",
    "file.write(analysis_result)\n",
    "file.close() "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Results & Conclusion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Random Forest is the best classfier for predicting employee attrition for our dataset. Some of the most important factors on which employee attrition depends are \n",
    "* Satisfaction Level\n",
    "* Tenure with organisation\n",
    "* Time since last evaluation\n",
    "* Work Accident\n",
    "* Salary\n",
    "* Department\n",
    "* Career Advancement ( If Promoted in last five years or not)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
