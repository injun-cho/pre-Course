{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial(n):\n",
    "    if n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n + factorial(n-1)\n",
    "\n",
    "print (factorial(int(input(\"Input Number for Factorial Calculation: \"))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial(n):\n",
    "    \n",
    "    res = 1\n",
    "    \n",
    "    while n == 1 : \n",
    "        \n",
    "        res = res*n\n",
    "        n = n -1\n",
    "    \n",
    "print (factorial(int(input(\"Input Number for Factorial Calculation: \"))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.10.8"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
