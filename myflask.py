from flask import Flask, render_template
import numpy as np
import pandas
import matplotlib.pyplot as plt

app = Flask(__name__)
count = 0

@app.route('/test')
def chartTest():
    global count 
    count = count + 1
  # x axis values 
    x = [1,2,3] 
    # corresponding y axis values 
    y = [2,4,1] 
        
    try:

        # plotting the points  
        plt.plot(x, y) 
        print("100")    
        # naming the x axis 
        plt.xlabel('x - axis') 
        # naming the y axis 
        plt.ylabel('y - axis') 

        print("111")    
        # giving a title to my graph 
        plt.title('My first graph!')    
        file = './static/images/' + str(count) + '/new_plot' + str(count) + '.png'
        print(' file = ' + file)
        plt.savefig(file)
        print("121")
    except Exception:

     # Just print traceback
        print ("something went wrong, here is some info:")
        traceback.print_exc()
    print("141") 
    return render_template('plot.html', name = file, url =file)

app.run(host='localhost', port=5000, debug=True)