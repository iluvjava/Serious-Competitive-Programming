## Intro

* A multi-set store the element along with a frequency, this is just a fancier version of the map where, the elements can be hashed perfectly, this design make things extremely fast when the set of symbols involved in a stream of data is sparse compare to the size of the stream. 
	* for example, a stream of data with length 10e7 but only contains the 26 letters of the alphabet. 

* A multi-set can be exploit to keep the median of a data stream using a 2 pointers to keep track of the median, and if it's sorted, it can also be used to improve the speed that deals with a stream of letters. 
	* [[Fraudulant Activity Notifications]]
		* Perfectly Hased multi-set to keep track of the median of the data string in real time. 
	* [[Reverse Shuffle Merge]]
		* Sorted Multi-set to model sequences of letters
	* [[Min Subarry Absolute Diff]]
		* Find the length of the longest subarray of the array such that, all pairs of numbers in the contiguous sub array is less than a given threadshold. 
		* Exploited: Using the mult-set to keep track of the minimal and maximal element for the sliding window.