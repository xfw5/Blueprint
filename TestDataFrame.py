from pandas import *
import numpy

if __name__ == '__main__':
    dates = date_range(start='2016-05-01', periods=4)
    data = numpy.random.randint(4,6 ,(4,4))
    df = DataFrame(data=data, index=dates, columns=['low', 'high', 'open', 'close'])
    df.close = [6, 6, 6, 6]
    #df.replace([4], [88], inplace=True)
    print df
    print df.columns
    print df.columns.values
    print df.values
    print df.index
   # for stock in df.columns.values:



    df[df<6] = None
    df = df.isnull()
    print df
    df[df == True] = None

    values = df.close.values
    print values
    #df = df.dropna(axis=1)
    #df.drop(labels=df.columns.values, axis=1, inplace=True)
    #df.drop(labels=df.index.values, axis=0, inplace=False)
    #print df
   # print df[df==True]
    # #
    # df = df.isin([5])
    # print df
    # print "\n"
    # df = df.filter(regex='True', axis=0)
    # print df