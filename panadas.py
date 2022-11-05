{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0c71a18b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#1.2.1 series\n",
    "\n",
    "import pandas as pd\n",
    "h=('AA','2012-02-01',100,10.2)\n",
    "s = pd.Series(h)\n",
    "\n",
    "type(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5e075d84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0            AA\n",
      "1    2012-02-01\n",
      "2           100\n",
      "3          10.2\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8f9a2a9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "d={'name ':'IBM','date' : '2010-09-08','price':10.2,'shates' :100 }\n",
    "ds = pd.Series(d)\n",
    "\n",
    "type=(ds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d2066703",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name             IBM\n",
      "date      2010-09-08\n",
      "price           10.2\n",
      "shates           100\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(ds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "35884728",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name              FB\n",
      "date      2001-08-02\n",
      "shares            90\n",
      "price            3.2\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    ">>> f = ['FB', '2001-08-02', 90, 3.2]\n",
    ">>> f = pd.Series(f, index = ['name', 'date', 'shares', 'price'])\n",
    ">>> print(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "71d61d69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'FB'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f['shares']\n",
    "90\n",
    "f[0]\n",
    "'FB'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6c59931e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "shares     90\n",
       "price     3.2\n",
       "dtype: object"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f[['shares','price']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af098951",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
