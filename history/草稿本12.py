Python 3.6.5 |Anaconda custom (64-bit)| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1414, in <module>
    dates=pd.data_range('20180603',periods=6)
AttributeError: module 'pandas' has no attribute 'data_range'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
Traceback (most recent call last):
  File "F:\anaconda\lib\site-packages\pandas\core\internals.py", line 4857, in create_block_manager_from_blocks
    placement=slice(0, len(axes[0])))]
  File "F:\anaconda\lib\site-packages\pandas\core\internals.py", line 3205, in make_block
    return klass(values, ndim=ndim, placement=placement)
  File "F:\anaconda\lib\site-packages\pandas\core\internals.py", line 125, in __init__
    '{mgr}'.format(val=len(self.values), mgr=len(self.mgr_locs)))
ValueError: Wrong number of items passed 4, placement implies 3

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1418, in <module>
    df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c'])
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 379, in __init__
    copy=copy)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 536, in _init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "F:\anaconda\lib\site-packages\pandas\core\internals.py", line 4866, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "F:\anaconda\lib\site-packages\pandas\core\internals.py", line 4843, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (3, 6)
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -1.173037  1.040204 -0.403729 -1.866158
2018-06-04 -1.396792  1.029127 -1.263079 -0.015374
2018-06-05 -0.029321  0.705545  0.765992  0.687266
2018-06-06  0.732891 -0.448206 -0.377536  0.987317
2018-06-07 -0.636798 -0.351443 -0.103980 -1.054735
2018-06-08 -0.160343 -1.305288 -0.965836  0.793554
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -2.087967 -0.172369 -2.284492 -0.345434
2018-06-04  2.188512 -0.657743 -0.203662  0.013993
2018-06-05 -0.101506 -1.544535  0.749802 -0.228279
2018-06-06  0.567917  0.899443  0.282796  1.149603
2018-06-07  0.377148 -0.581650  1.289016 -0.814586
2018-06-08  0.331774 -1.513046 -1.516844  1.036512
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  0.229088  1.684509 -1.054976  0.498723
2018-06-04  0.370057  0.780092 -0.988412  0.096865
2018-06-05 -1.420078 -0.021687 -0.621290 -0.580479
2018-06-06 -0.578479 -0.628311  0.837049  0.863559
2018-06-07 -0.170820  0.449368 -0.026916  0.859274
2018-06-08 -0.776951  0.984536 -0.039505  0.385458
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1429, in <module>
    df2=pd.DateFrame({'A':1.,
AttributeError: module 'pandas' has no attribute 'DateFrame'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -1.295840 -0.204497  0.483496 -2.074365
2018-06-04  0.258451  0.558496 -1.328029 -1.307994
2018-06-05 -0.478705  0.170434  0.797871 -0.346793
2018-06-06 -0.150957 -1.359042 -0.004697 -0.782321
2018-06-07 -1.321427  2.375772  0.360192  2.266394
2018-06-08 -1.778553 -1.199273 -1.479786  0.636877
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
>>> print(df2.B)
		      
0   2018-06-03
1   2018-06-03
2   2018-06-03
3   2018-06-03
Name: B, dtype: datetime64[ns]
>>> print(df2.A)
		      
0    1.0
1    1.0
2    1.0
3    1.0
Name: A, dtype: float64
>>> print(df2['A'])
		      
0    1.0
1    1.0
2    1.0
3    1.0
Name: A, dtype: float64
>>> print(df2[A])
		      
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(df2[A])
NameError: name 'A' is not defined
>>> print(df2['B'])
		      
0   2018-06-03
1   2018-06-03
2   2018-06-03
3   2018-06-03
Name: B, dtype: datetime64[ns]
>>> print(df2.C)
		      
0    1.0
1    1.0
2    1.0
3    1.0
Name: C, dtype: float32
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  1.849523 -0.021174 -0.623897 -0.687887
2018-06-04 -0.490385 -0.979292  0.390466  0.400726
2018-06-05  0.371980 -0.683866 -1.479397 -2.900420
2018-06-06  0.552617 -1.331033  0.624994 -0.775204
2018-06-07 -0.226329 -2.236675 -1.419101  0.905772
2018-06-08 -0.872170  0.370401  0.361738 -0.849221
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1434, in <module>
    'F':'foo'})
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 348, in __init__
    mgr = self._init_dict(data, index, columns, dtype=dtype)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 459, in _init_dict
    return _arrays_to_mgr(arrays, data_names, index, columns, dtype=dtype)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 7315, in _arrays_to_mgr
    index = extract_index(arrays)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 7371, in extract_index
    raise ValueError(msg)
ValueError: array length 4 does not match index length 3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  1.643204 -0.401081  1.331783 -0.908268
2018-06-04 -1.163496  1.634008  1.892193 -0.514492
2018-06-05 -0.974481 -0.581666 -0.221153  0.534008
2018-06-06 -1.277070 -0.004414  0.567632  0.987736
2018-06-07  0.656860  0.835800 -0.386895  0.673744
2018-06-08 -0.028527  0.572463  0.319740  0.920863
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1434, in <module>
    'F':'foo'})
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 348, in __init__
    mgr = self._init_dict(data, index, columns, dtype=dtype)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 459, in _init_dict
    return _arrays_to_mgr(arrays, data_names, index, columns, dtype=dtype)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 7315, in _arrays_to_mgr
    index = extract_index(arrays)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 7361, in extract_index
    raise ValueError('arrays must all be same length')
ValueError: arrays must all be same length
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -1.641530 -0.365257  2.484730  0.809624
2018-06-04  0.553792 -1.246630 -0.245639 -0.447276
2018-06-05 -0.060448 -0.176132 -1.965386 -0.726316
2018-06-06  1.330426 -0.069393  1.319845 -1.073211
2018-06-07 -0.963893  0.031446 -1.173884 -0.268208
2018-06-08 -0.791723 -1.786281 -0.976459  0.651038
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D          E    F
0  1.0 2018-06-03  1.0  3       test  foo
1  1.0 2018-06-03  1.0  3      train  foo
2  1.0 2018-06-03  1.0  3  testtrain  foo
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -0.015792  0.217931  0.425769 -1.592187
2018-06-04 -0.231875  1.208707  0.550121  1.070472
2018-06-05  0.623539  0.008305 -0.072453  0.763727
2018-06-06  0.507545  0.846422  1.239775  0.805603
2018-06-07 -0.766052  0.271027  0.115838 -2.414163
2018-06-08  1.342048 -0.035729 -0.357151  0.508946
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1434, in <module>
    'F':'foo'})
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 348, in __init__
    mgr = self._init_dict(data, index, columns, dtype=dtype)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 459, in _init_dict
    return _arrays_to_mgr(arrays, data_names, index, columns, dtype=dtype)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 7315, in _arrays_to_mgr
    index = extract_index(arrays)
  File "F:\anaconda\lib\site-packages\pandas\core\frame.py", line 7361, in extract_index
    raise ValueError('arrays must all be same length')
ValueError: arrays must all be same length
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -0.088728  0.829818 -0.804179 -0.831023
2018-06-04  1.984369 -1.433291 -0.246241  0.376622
2018-06-05 -0.858860  0.550197  1.459719  0.548926
2018-06-06  1.944715  0.330126  1.511511 -0.233521
2018-06-07 -1.954042 -0.247323 -0.594983  0.197761
2018-06-08  0.330417  0.991783  0.318144 -0.526423
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  0.706054  1.725930 -0.412065  2.651706
2018-06-04 -0.380594  0.560057  0.619279  1.535002
2018-06-05 -2.012248  1.302552  1.079404  0.363708
2018-06-06  1.018812  1.251828  0.078492  0.056024
2018-06-07  1.158697  1.100309 -0.180854  0.226710
2018-06-08 -0.632506  0.147240  0.335939 -0.006838
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  0.382581 -0.430214 -1.666610 -0.202846
2018-06-04  0.438196 -0.267529  0.046912 -0.043516
2018-06-05 -0.342211 -0.774271  2.384741  0.600729
2018-06-06 -0.168270 -1.319523  0.260920 -0.223208
2018-06-07  0.964531  0.793059 -0.867055 -0.607794
2018-06-08 -0.679245  1.573474  0.963720 -0.663195
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  0.925533 -0.128667  0.844601 -0.498250
2018-06-04 -0.716661 -2.046573  1.671542  1.219294
2018-06-05 -0.527107 -1.390768  0.299369 -0.095795
2018-06-06  0.709240  0.238435  0.714374 -1.228579
2018-06-07 -0.761532 -0.190617  1.226923  0.807476
2018-06-08  0.681663 -0.354613  1.157613  0.167553
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -2.317561 -1.185888  0.045871  0.413042
2018-06-04  0.979395 -1.059980 -0.574628 -0.111309
2018-06-05  0.086913  1.000060 -1.251345  0.283276
2018-06-06  0.963880  1.831530 -0.878763 -0.415322
2018-06-07 -1.078998  0.703887 -0.317149 -0.295628
2018-06-08  0.951530 -0.514809  0.369046 -1.849088
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -0.691248 -0.130503 -1.201226 -0.393858
2018-06-04  0.806775  0.307675 -0.396195 -0.289873
2018-06-05 -1.143769 -1.405703 -0.594857  0.353516
2018-06-06  1.102684 -0.650693  0.582370 -0.690786
2018-06-07  0.621520 -0.294727 -0.054463 -0.299535
2018-06-08  0.739085 -1.265272 -1.003108  2.151268
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
<bound method NDFrame.describe of      A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo>
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  1.618864 -0.810360 -0.546649 -0.644386
2018-06-04  0.851275 -0.068874  0.666400 -1.283336
2018-06-05 -0.763219  0.150410 -0.325022  0.065946
2018-06-06  0.360301 -0.673178 -0.219327 -0.385583
2018-06-07  2.055211 -0.548053 -0.052805 -0.083031
2018-06-08  0.789165 -1.856813 -1.446592 -1.720025
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -1.329062 -0.280393 -0.262339 -1.342558
2018-06-04  1.442440  1.402342  0.248293  0.312736
2018-06-05  0.498970 -0.472610 -0.578813  1.514464
2018-06-06  1.002655  0.586643 -1.978981  0.064619
2018-06-07  0.050575 -0.442993 -0.294336  2.046048
2018-06-08  1.940469  0.976434 -0.077053  1.002538
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
                     0                    1                    2                    3
A                    1                    1                    1                    1
B  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00
C                    1                    1                    1                    1
D                    3                    3                    3                    3
E                 test                train                 test                train
F                  foo                  foo                  foo                  foo
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -1.973023 -0.301153 -0.832102 -0.233757
2018-06-04 -0.416870  2.372772 -1.063371  0.559310
2018-06-05  0.063819  0.229477 -1.075060  0.328577
2018-06-06 -0.154678 -0.679736 -1.262356 -1.360038
2018-06-07 -0.945266 -0.094966  0.844577  1.366633
2018-06-08 -1.487602 -0.732317  0.519376  0.625210
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
                     0                    1                    2                    3
A                    1                    1                    1                    1
B  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00
C                    1                    1                    1                    1
D                    3                    3                    3                    3
E                 test                train                 test                train
F                  foo                  foo                  foo                  foo
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1442, in <module>
    print(df2.sort_index(aixs=1,ascending=False))
TypeError: sort_index() got an unexpected keyword argument 'aixs'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -0.518479 -0.623497  0.885336  1.399884
2018-06-04 -0.279682  0.034942  0.735629  0.981964
2018-06-05 -1.230079 -0.161255  0.430018  0.517380
2018-06-06 -0.516843 -0.627550  1.455305 -2.405893
2018-06-07 -0.316349  0.451660  0.290010 -0.610959
2018-06-08 -0.965741  1.748255  1.622071  0.452316
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
                     0                    1                    2                    3
A                    1                    1                    1                    1
B  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00
C                    1                    1                    1                    1
D                    3                    3                    3                    3
E                 test                train                 test                train
F                  foo                  foo                  foo                  foo
     F      E  D    C          B    A
0  foo   test  3  1.0 2018-06-03  1.0
1  foo  train  3  1.0 2018-06-03  1.0
2  foo   test  3  1.0 2018-06-03  1.0
3  foo  train  3  1.0 2018-06-03  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03  1.111119  0.255956  0.947503 -1.503935
2018-06-04  0.282970 -0.339000 -0.895428  0.248560
2018-06-05  1.861120  0.045491  0.346956  0.656638
2018-06-06 -1.991509  1.297617 -1.189453 -0.205902
2018-06-07  0.274191 -0.348081  0.210929  0.776909
2018-06-08 -1.500056 -1.095000  0.296335 -0.892385
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
                     0                    1                    2                    3
A                    1                    1                    1                    1
B  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00
C                    1                    1                    1                    1
D                    3                    3                    3                    3
E                 test                train                 test                train
F                  foo                  foo                  foo                  foo
     F      E  D    C          B    A
0  foo   test  3  1.0 2018-06-03  1.0
1  foo  train  3  1.0 2018-06-03  1.0
2  foo   test  3  1.0 2018-06-03  1.0
3  foo  train  3  1.0 2018-06-03  1.0
     A          B    C  D      E    F
3  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
0  1.0 2018-06-03  1.0  3   test  foo
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06',
               '2018-06-07', '2018-06-08'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2018-06-03 -0.172496  0.868003  0.745693 -0.986183
2018-06-04  1.296947  2.127871 -1.066313  0.461538
2018-06-05  0.139932 -0.752073  1.130166  0.501031
2018-06-06 -2.174375  0.651544 -0.523981  0.923265
2018-06-07 -0.426448  0.058239  0.191427  2.206109
2018-06-08 -1.055650  0.788753  0.970964 -0.696415
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Int64Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2018-06-03 00:00:00') 1.0 3 'train' 'foo']]
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
                     0                    1                    2                    3
A                    1                    1                    1                    1
B  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00  2018-06-03 00:00:00
C                    1                    1                    1                    1
D                    3                    3                    3                    3
E                 test                train                 test                train
F                  foo                  foo                  foo                  foo
     F      E  D    C          B    A
0  foo   test  3  1.0 2018-06-03  1.0
1  foo  train  3  1.0 2018-06-03  1.0
2  foo   test  3  1.0 2018-06-03  1.0
3  foo  train  3  1.0 2018-06-03  1.0
     A          B    C  D      E    F
3  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
0  1.0 2018-06-03  1.0  3   test  foo
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
2  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
3  1.0 2018-06-03  1.0  3  train  foo
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
Traceback (most recent call last):
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\datetimes.py", line 1613, in get_loc
    return Index.get_loc(self, key, method, tolerance)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 3063, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 419, in pandas._libs.index.DatetimeEngine.get_loc
  File "pandas\_libs\index.pyx", line 421, in pandas._libs.index.DatetimeEngine.get_loc
TypeError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1464, in <module>
    print(df.loc[:['A','B']])
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1478, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1866, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1511, in _get_slice_axis
    slice_obj.step, kind=self.name)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\datetimes.py", line 1706, in slice_indexer
    return Index.slice_indexer(self, start, end, step, kind=kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4090, in slice_indexer
    kind=kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4297, in slice_locs
    end_slice = self.get_slice_bound(end, 'right', kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4221, in get_slice_bound
    slc = self._get_loc_only_exact_matches(label)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4190, in _get_loc_only_exact_matches
    return self.get_loc(key)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\datetimes.py", line 1621, in get_loc
    stamp = Timestamp(key, tz=self.tz)
  File "pandas\_libs\tslibs\timestamps.pyx", line 635, in pandas._libs.tslibs.timestamps.Timestamp.__new__
  File "pandas\_libs\tslibs\conversion.pyx", line 309, in pandas._libs.tslibs.conversion.convert_to_tsobject
TypeError: Cannot convert input [['A', 'B']] of type <class 'list'> to Timestamp
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1473, in <module>
    prin(df.ix[:3,['A','C']])
NameError: name 'prin' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1474, in <module>
    print(df.loc[:3,['A','C']])
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1472, in __getitem__
    return self._getitem_tuple(key)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 890, in _getitem_tuple
    retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1866, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1511, in _get_slice_axis
    slice_obj.step, kind=self.name)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\datetimes.py", line 1706, in slice_indexer
    return Index.slice_indexer(self, start, end, step, kind=kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4090, in slice_indexer
    kind=kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4297, in slice_locs
    end_slice = self.get_slice_bound(end, 'right', kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4217, in get_slice_bound
    label = self._maybe_cast_slice_bound(label, side, kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\datetimes.py", line 1653, in _maybe_cast_slice_bound
    self._invalid_indexer('slice', label)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 1848, in _invalid_indexer
    kind=type(key)))
TypeError: cannot do slice indexing on <class 'pandas.core.indexes.datetimes.DatetimeIndex'> with these indexers [3] of <class 'int'>
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1475, in <module>
    print(df.iloc[:3,['A','C']])
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1472, in __getitem__
    return self._getitem_tuple(key)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 2013, in _getitem_tuple
    self._has_valid_tuple(tup)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 222, in _has_valid_tuple
    self._validate_key(k, i)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1967, in _validate_key
    if len(arr) and (arr.max() >= l or arr.min() < -l):
  File "F:\anaconda\lib\site-packages\numpy\core\_methods.py", line 26, in _amax
    return umr_maximum(a, axis, None, out, keepdims)
TypeError: cannot perform reduce with flexible type
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1475, in <module>
    print(df.iloc[:3,[0,4]])
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1472, in __getitem__
    return self._getitem_tuple(key)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 2013, in _getitem_tuple
    self._has_valid_tuple(tup)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 222, in _has_valid_tuple
    self._validate_key(k, i)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1968, in _validate_key
    raise IndexError("positional indexers are out-of-bounds")
IndexError: positional indexers are out-of-bounds
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
            B   D
2018-06-03  1   3
2018-06-04  5   7
2018-06-05  9  11
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
            A   D
2018-06-03  0   3
2018-06-04  4   7
2018-06-05  8  11
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1474, in <module>
    print(df.loc[:3,['A','C']])
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1472, in __getitem__
    return self._getitem_tuple(key)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 890, in _getitem_tuple
    retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1866, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "F:\anaconda\lib\site-packages\pandas\core\indexing.py", line 1511, in _get_slice_axis
    slice_obj.step, kind=self.name)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\datetimes.py", line 1706, in slice_indexer
    return Index.slice_indexer(self, start, end, step, kind=kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4090, in slice_indexer
    kind=kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4297, in slice_locs
    end_slice = self.get_slice_bound(end, 'right', kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 4217, in get_slice_bound
    label = self._maybe_cast_slice_bound(label, side, kind)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\datetimes.py", line 1653, in _maybe_cast_slice_bound
    self._invalid_indexer('slice', label)
  File "F:\anaconda\lib\site-packages\pandas\core\indexes\base.py", line 1848, in _invalid_indexer
    kind=type(key)))
TypeError: cannot do slice indexing on <class 'pandas.core.indexes.datetimes.DatetimeIndex'> with these indexers [3] of <class 'int'>
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
             A   C
2018-06-03   0   2
2018-06-04   4   6
2018-06-05   8  10
2018-06-06  12  14
2018-06-07  16  18
2018-06-08  20  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
             A   C
2018-06-03   0   2
2018-06-04   4   6
2018-06-05   8  10
2018-06-06  12  14
2018-06-07  16  18
2018-06-08  20  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
             A   B   C   D
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
             A   C
2018-06-03   0   2
2018-06-04   4   6
2018-06-05   8  10
2018-06-06  12  14
2018-06-07  16  18
2018-06-08  20  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
             A   B   C   D
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
2018-06-03     0
2018-06-04     4
2018-06-05     8
2018-06-06    12
2018-06-07    16
2018-06-08    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
            A  B   C   D
2018-06-03  0  1   2   3
2018-06-04  4  5   6   7
2018-06-05  8  9  10  11
A    0
B    1
C    2
D    3
Name: 2018-06-03 00:00:00, dtype: int32
             A   B
2018-06-03   0   1
2018-06-04   4   5
2018-06-05   8   9
2018-06-06  12  13
2018-06-07  16  17
2018-06-08  20  21
             B   C
2018-06-06  13  14
2018-06-07  17  18
             B   C
2018-06-04   5   6
2018-06-06  13  14
2018-06-08  21  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
             A   C
2018-06-03   0   2
2018-06-04   4   6
2018-06-05   8  10
2018-06-06  12  14
2018-06-07  16  18
2018-06-08  20  22
            A   C
2018-06-03  0   2
2018-06-04  4   6
2018-06-05  8  10
             A   B   C   D
2018-06-03   0   1   2   3
2018-06-04   4   5   6   7
2018-06-05   8   9  10  11
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
             A   B   C   D
2018-06-06  12  13  14  15
2018-06-07  16  17  18  19
2018-06-08  20  21  22  23
2018-06-03    False
2018-06-04    False
2018-06-05    False
2018-06-06     True
2018-06-07     True
2018-06-08     True
Freq: D, Name: A, dtype: bool
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A   B     C   D
2018-06-03   0   1     2   3
2018-06-04   4   5     6   7
2018-06-05   8   9  1111  11
2018-06-06  12  13    14  15
2018-06-07  16  17    18  19
2018-06-08  20  21    22  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A    B     C   D
2018-06-03   0  222     2   3
2018-06-04   4    5     6   7
2018-06-05   8    9  1111  11
2018-06-06  12   13    14  15
2018-06-07  16   17    18  19
2018-06-08  20   21    22  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  0    0  0  0
2018-06-05  0    0  0  0
2018-06-06  0    0  0  0
2018-06-07  0    0  0  0
2018-06-08  0    0  0  0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A    B     C   D
2018-06-03   0  222     2   3
2018-06-04   4    5     6   7
2018-06-05   8    9  1111  11
2018-06-06  12   13    14  15
2018-06-07  16   17    18  19
2018-06-08  20   21    22  23
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  0    0  0  0
2018-06-05  0    0  0  0
2018-06-06  0    0  0  0
2018-06-07  0    0  0  0
2018-06-08  0    0  0  0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A    B     C   D
2018-06-03   0  222     2   3
2018-06-04   4    5     6   7
2018-06-05   8    9  1111  11
2018-06-06  12   13    14  15
2018-06-07  16   17    18  19
2018-06-08  20   21    22  23
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  0    0  0  0
2018-06-06  0    0  0  0
2018-06-07  0    0  0  0
2018-06-08  0    0  0  0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A    B     C   D
2018-06-03   0  222     2   3
2018-06-04   4    5     6   7
2018-06-05   8    9  1111  11
2018-06-06  12   13    14  15
2018-06-07  16   17    18  19
2018-06-08  20   21    22  23
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  0    0  0  0
2018-06-06  0    0  0  0
2018-06-07  0    0  0  0
2018-06-08  0    0  0  0
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  0    0  0  0
2018-06-06  0    0  0  0
2018-06-07  0    0  0  0
2018-06-08  0    0  0  0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A    B     C   D
2018-06-03   0  222     2   3
2018-06-04   4    5     6   7
2018-06-05   8    9  1111  11
2018-06-06  12   13    14  15
2018-06-07  16   17    18  19
2018-06-08  20   21    22  23
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  5    5  5  5
2018-06-06  5    5  5  5
2018-06-07  5    5  5  5
2018-06-08  5    5  5  5
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  0    5  5  5
2018-06-06  0    5  5  5
2018-06-07  0    5  5  5
2018-06-08  0    5  5  5
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A    B     C   D
2018-06-03   0  222     2   3
2018-06-04   4    5     6   7
2018-06-05   8    9  1111  11
2018-06-06  12   13    14  15
2018-06-07  16   17    18  19
2018-06-08  20   21    22  23
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  5    5  5  5
2018-06-06  5    5  5  5
2018-06-07  5    5  5  5
2018-06-08  5    5  5  5
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  0    5  5  5
2018-06-06  0    5  5  5
2018-06-07  0    5  5  5
2018-06-08  0    5  5  5
            A    B  C  D   F
2018-06-03  0  222  2  3 NaN
2018-06-04  4    5  6  7 NaN
2018-06-05  0    5  5  5 NaN
2018-06-06  0    5  5  5 NaN
2018-06-07  0    5  5  5 NaN
2018-06-08  0    5  5  5 NaN
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A    B     C   D
2018-06-03   0  222     2   3
2018-06-04   4    5     6   7
2018-06-05   8    9  1111  11
2018-06-06  12   13    14  15
2018-06-07  16   17    18  19
2018-06-08  20   21    22  23
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  5    5  5  5
2018-06-06  5    5  5  5
2018-06-07  5    5  5  5
2018-06-08  5    5  5  5
            A    B  C  D
2018-06-03  0  222  2  3
2018-06-04  4    5  6  7
2018-06-05  0    5  5  5
2018-06-06  0    5  5  5
2018-06-07  0    5  5  5
2018-06-08  0    5  5  5
            A    B  C  D   F
2018-06-03  0  222  2  3 NaN
2018-06-04  4    5  6  7 NaN
2018-06-05  0    5  5  5 NaN
2018-06-06  0    5  5  5 NaN
2018-06-07  0    5  5  5 NaN
2018-06-08  0    5  5  5 NaN
            A    B  C  D   F  E
2018-06-03  0  222  2  3 NaN  1
2018-06-04  4    5  6  7 NaN  2
2018-06-05  0    5  5  5 NaN  3
2018-06-06  0    5  5  5 NaN  4
2018-06-07  0    5  5  5 NaN  5
2018-06-08  0    5  5  5 NaN  6
>>> s=pd.Series([1,3,6,np.nan,44,1])
>>> print(s)
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1519, in <module>
    df=pd.DataFranme(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
AttributeError: module 'pandas' has no attribute 'DataFranme'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A   D
2018-06-03   0   3
2018-06-04   4   7
2018-06-05   8  11
2018-06-06  12  15
2018-06-07  16  19
2018-06-08  20  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-03   0   0.0   2.0   3
2018-06-04   4   5.0   0.0   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-03   0   0.0   2.0   3
2018-06-04   4   5.0   0.0   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
                A      B      C      D
2018-06-03  False   True  False  False
2018-06-04  False  False   True  False
2018-06-05  False  False  False  False
2018-06-06  False  False  False  False
2018-06-07  False  False  False  False
2018-06-08  False  False  False  False
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-03   0   0.0   2.0   3
2018-06-04   4   5.0   0.0   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
                A      B      C      D
2018-06-03  False   True  False  False
2018-06-04  False  False   True  False
2018-06-05  False  False  False  False
2018-06-06  False  False  False  False
2018-06-07  False  False  False  False
2018-06-08  False  False  False  False
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-03   0   0.0   2.0   3
2018-06-04   4   5.0   0.0   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
             A     B     C   D
2018-06-03   0   NaN   2.0   3
2018-06-04   4   5.0   NaN   7
2018-06-05   8   9.0  10.0  11
2018-06-06  12  13.0  14.0  15
2018-06-07  16  17.0  18.0  19
2018-06-08  20  21.0  22.0  23
                A      B      C      D
2018-06-03  False   True  False  False
2018-06-04  False  False   True  False
2018-06-05  False  False  False  False
2018-06-06  False  False  False  False
2018-06-07  False  False  False  False
2018-06-08  False  False  False  False
True
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1540, in <module>
    data=pd.read_csv('student.csv')
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'student.csv' does not exist
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    Student ID  name   age  gender
0         1100  Kelly   22  Female
1         1101    Clo   21  Female
2         1102  Tilly   22  Female
3         1103   Tony   24    Male
4         1104  David   20    Male
5         1105  Catty   22  Female
6         1106      M    3  Female
7         1107      N   43    Male
8         1108      A   13    Male
9         1109      S   12    Male
10        1110  David   33    Male
11        1111     Dw    3  Female
12        1112      Q   23    Male
13        1113      W   21  Female
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    Student ID  name   age  gender
0         1100  Kelly   22  Female
1         1101    Clo   21  Female
2         1102  Tilly   22  Female
3         1103   Tony   24    Male
4         1104  David   20    Male
5         1105  Catty   22  Female
6         1106      M    3  Female
7         1107      N   43    Male
8         1108      A   13    Male
9         1109      S   12    Male
10        1110  David   33    Male
11        1111     Dw    3  Female
12        1112      Q   23    Male
13        1113      W   21  Female
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1543, in <module>
    a=pd.read_py('code.py')
AttributeError: module 'pandas' has no attribute 'read_py'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    Student ID  name   age  gender
0         1100  Kelly   22  Female
1         1101    Clo   21  Female
2         1102  Tilly   22  Female
3         1103   Tony   24    Male
4         1104  David   20    Male
5         1105  Catty   22  Female
6         1106      M    3  Female
7         1107      N   43    Male
8         1108      A   13    Male
9         1109      S   12    Male
10        1110  David   33    Male
11        1111     Dw    3  Female
12        1112      Q   23    Male
13        1113      W   21  Female
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1543, in <module>
    a=pd.read_csv('新建文本文档.txt')
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "F:\anaconda\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 697, in pandas._libs.parsers.TextReader._setup_parser_source
OSError: Initializing from file failed
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    Student ID  name   age  gender
0         1100  Kelly   22  Female
1         1101    Clo   21  Female
2         1102  Tilly   22  Female
3         1103   Tony   24    Male
4         1104  David   20    Male
5         1105  Catty   22  Female
6         1106      M    3  Female
7         1107      N   43    Male
8         1108      A   13    Male
9         1109      S   12    Male
10        1110  David   33    Male
11        1111     Dw    3  Female
12        1112      Q   23    Male
13        1113      W   21  Female
Empty DataFrame
Columns: [111231231231]
Index: []
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    Student ID  name   age  gender
0         1100  Kelly   22  Female
1         1101    Clo   21  Female
2         1102  Tilly   22  Female
3         1103   Tony   24    Male
4         1104  David   20    Male
5         1105  Catty   22  Female
6         1106      M    3  Female
7         1107      N   43    Male
8         1108      A   13    Male
9         1109      S   12    Male
10        1110  David   33    Male
11        1111     Dw    3  Female
12        1112      Q   23    Male
13        1113      W   21  Female
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    Student ID  name   age  gender
0         1100  Kelly   22  Female
1         1101    Clo   21  Female
2         1102  Tilly   22  Female
3         1103   Tony   24    Male
4         1104  David   20    Male
5         1105  Catty   22  Female
6         1106      M    3  Female
7         1107      N   43    Male
8         1108      A   13    Male
9         1109      S   12    Male
10        1110  David   33    Male
11        1111     Dw    3  Female
12        1112      Q   23    Male
13        1113      W   21  Female
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1565, in <module>
    res=pd,concat([df1,df2,df3],axis=0)
NameError: name 'concat' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],axis=0,ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],axis=0)#,ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2])#,ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  0.0  0.0  0.0  0.0  NaN
2  NaN  1.0  1.0  1.0  1.0
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
0  0.0  0.0  0.0  0.0  NaN
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
5  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],axis=0,ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
0  0.0  0.0  0.0  0.0  NaN
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
5  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
     0    1    2    3    4    5    6    7
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
     a    b    c    d    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],axis=0,join='outer')#,ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  0.0  0.0  0.0  0.0  NaN
2  NaN  1.0  1.0  1.0  1.0
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],axis=0,join='outer',ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
0  0.0  0.0  0.0  0.0  NaN
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
5  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],join='outer',ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
0  0.0  0.0  0.0  0.0  NaN
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
5  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],axis=0,join='outer',ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
0  0.0  0.0  0.0  0.0  NaN
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
5  NaN  1.0  1.0  1.0  1.0
     b    c    d
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0
3  1.0  1.0  1.0
4  1.0  1.0  1.0
5  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
     b    c    d
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0
3  1.0  1.0  1.0
4  1.0  1.0  1.0
5  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0

Warning (from warnings module):
  File "C:\Users\Administrator\Desktop\code.py", line 1580
    res=pd.concat([df1,df2],axis=0,join='outer',ignore_index=True)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=True'.

To retain the current behavior and silence the warning, pass sort=False

     a    b    c    d    e
0  0.0  0.0  0.0  0.0  NaN
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
5  NaN  1.0  1.0  1.0  1.0
     b    c    d
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0
3  1.0  1.0  1.0
4  1.0  1.0  1.0
5  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0
     a    b    c    d    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1619, in <module>
    res=df1.append([df2,df3],axis=1,ignore_index=True)         #-----和合并的两种方法
TypeError: append() got an unexpected keyword argument 'axis'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  2.0  3.0  4.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  2.0  3.0  4.0
a    1
b    2
c    3
d    4
dtype: int64
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A          B    C  D      E    F
0  1.0 2018-06-03  1.0  3   test  foo
1  1.0 2018-06-03  1.0  3  train  foo
2  1.0 2018-06-03  1.0  3   test  foo
3  1.0 2018-06-03  1.0  3  train  foo
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1654, in <module>
    res=pd.merge(left.right,on='key')
  File "F:\anaconda\lib\site-packages\pandas\core\generic.py", line 4372, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'right'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key   A   B
0  K0  A0  B0
1  K2  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K2  A1  B1  C2  D2
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key   A   B
0  K0  A0  B0
1  K4  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K2  A2  B2  C2  D2
2  K3  A3  B3  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1686, in <module>
    res=pd.merge(left,right,on=['key1','key2'],how=right)
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 61, in merge
    return op.get_result()
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 567, in get_result
    join_index, left_indexer, right_indexer = self._get_join_info()
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 776, in _get_join_info
    right_indexer) = self._get_join_indexers()
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 755, in _get_join_indexers
    how=self.how)
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 1138, in _get_join_indexers
    if how == 'left':
  File "F:\anaconda\lib\site-packages\pandas\core\generic.py", line 1573, in __nonzero__
    .format(self.__class__.__name__))
ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
  key1 key2    A    B   C   D
0   K0   K0   A0   B0  C0  D0
1   K1   K0   A2   B2  C1  D1
2   K1   K0   A2   B2  C2  D2
3   K2   K0  NaN  NaN  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
  key1 key2   A   B    C    D
0   K0   K0  A0  B0   C0   D0
1   K0   K1  A1  B1  NaN  NaN
2   K1   K0  A2  B2   C1   D1
3   K1   K0  A2  B2   C2   D2
4   K2   K1  A3  B3  NaN  NaN
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
   col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
   col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
   col1 col_left  col_right      _merge
0     0        a        NaN   left_only
1     1        b        2.0        both
2     2      NaN        2.0  right_only
3     2      NaN        2.0  right_only
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
   col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
   col1 col_left  col_right
0     0        a        NaN
1     1        b        2.0
2     2      NaN        2.0
3     2      NaN        2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
   col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
   col1 col_left  col_right      _merge
0     0        a        NaN   left_only
1     1        b        2.0        both
2     2      NaN        2.0  right_only
3     2      NaN        2.0  right_only
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
   col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
   col1 col_left  col_right      _merge
0     0        a        NaN   left_only
1     1        b        2.0        both
2     2      NaN        2.0  right_only
3     2      NaN        2.0  right_only
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
   col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
   col1 col_left  col_right      _merge
0     0        a        NaN   left_only
1     1        b        2.0        both
2     2      NaN        2.0  right_only
3     2      NaN        2.0  right_only
   col1 col_left  col_right indicator_column
0     0        a        NaN        left_only
1     1        b        2.0             both
2     2      NaN        2.0       right_only
3     2      NaN        2.0       right_only
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1736, in <module>
    res=pd.merge(left,right,how='outer')
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 60, in merge
    validate=validate)
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 545, in __init__
    self._validate_specification()
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 1029, in _validate_specification
    lidx=self.left_index, ridx=self.right_index))
pandas.errors.MergeError: No common columns to perform merge on. Merge options: left_on=None, right_on=None, left_index=False, right_index=False
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1736, in <module>
    res=pd.merge(left,right,on=index,how='outer')
NameError: name 'index' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1736, in <module>
    res=pd.merge(left,right,on='index',how='outer')
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 60, in merge
    validate=validate)
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 550, in __init__
    self.join_names) = self._get_merge_keys()
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 856, in _get_merge_keys
    rk, stacklevel=stacklevel))
  File "F:\anaconda\lib\site-packages\pandas\core\generic.py", line 1379, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'index'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 1731, in <module>
    res=pd.merge(left,right,left_index=True,how='outer') #----根据索引值来填充
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 60, in merge
    validate=validate)
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 545, in __init__
    self._validate_specification()
  File "F:\anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 1015, in _validate_specification
    raise MergeError('Must pass right_on or right_index=True')
pandas.errors.MergeError: Must pass right_on or right_index=True
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    k  age
0  K0    1
1  K1    2
2  K2    3
    k  age
0  K0    4
1  K0    5
2  K3    6
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    k  age
0  K0    1
1  K1    2
2  K2    3
    k  age
0  K0    4
1  K0    5
2  K3    6
    k  age_boy  age_girl
0  K0        1         4
1  K0        1         5
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
    k  age
0  K0    1
1  K1    2
2  K2    3
    k  age
0  K0    4
1  K0    5
2  K3    6
    k  age_boy  age_girl
0  K0        1         4
1  K0        1         5
    k  age_boy  age_girl
0  K0      1.0       4.0
1  K0      1.0       5.0
2  K1      2.0       NaN
3  K2      3.0       NaN
4  K3      NaN       6.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============

============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============

============== RESTART: C:\Users\Administrator\Desktop\code.py ==============

============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0    1.767432
1    0.387797
2   -0.506856
3    0.117821
4    0.216078
5   -1.103135
6    0.071781
7    0.360729
8    1.768431
9   -1.265763
dtype: float64

============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0   -0.237256
1    3.438933
2   -0.031428
3   -1.053736
4   -1.568654
5   -0.061986
6   -0.488087
7   -1.885574
8   -1.323961
9   -0.608314
dtype: float64

============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0    0.399987
1   -0.803822
2    1.570323
3    1.120279
4    0.028365
5   -1.090989
6    1.694233
7   -0.016914
8    1.431118
9   -1.679208
dtype: float64
>>> 
