This is a python interface to Monument model serving.

Requirements:

* Monument gui version 1.14 or later

* python 3 with numpy (tested with python 3.8)

Method:

* create and save a Monument model

* select a csv file for model serving

* use the test.py script as a template for calling the server. You will need to specify:

  * maifile  - the Monument file saved after running a model
  * csvfile  - the data file to be served
  * algo     - the algo to be called

These definitions must match the model in the maifile.

For example, run the Monument application, then menu Help|Demos|Insurers and save, for example to `insure.mai`.

Copy the `insure2.csv` file in the repo to the same directory. Note that this file and the insure demo data in Monument contain random values.

Copy test.py to a new script, e.g. demo.py. Update the new script with the directories used for the two files. Then run the script, using

~~~~
   run.command       macos, linux
   run.cmd           windows
~~~~

For example:

~~~~
~/monument$ ./run.command demo.py
Ent-Boost(AIG):
[0, [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 84.266975306, 83.456123554, 83.679003499, 83.922832468, 83.227100486, 82.136659608, 78.618343321, 79.206285358, 78.956238572, 77.3779471, 80.624277601, 77.35610506, 75.990184392, 77.118267567, 77.539357834, 83.413333175, 78.771760555, 87.582798411]]
-----------------
LightGBM(MET):
[0, [None, None, None, None, None, None, None, None, None, None, 70.347962976, 73.729574441, 74.177049298, 76.60359986, 78.540167867, 77.743111935, 76.62659741, 76.21243108, 76.004730501, 76.696084498, 72.799332191, 75.723403363, 77.695306181, 80.571822401, 78.51396662, 80.981662204, 78.29077038, 77.587885817, 79.87918814, 81.641283798, 81.863832669, 79.108968194, 77.755798659, 74.463372438, 72.033799787, 75.703130468, 75.215633618, 73.379521242, 70.60071591, 70.914619537]]
