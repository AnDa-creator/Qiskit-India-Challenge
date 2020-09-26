# the write_and_run function writes the content in this cell into the file "feature_map.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START

# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, PauliFeatureMap
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def feature_map(): 
    # BUILD FEATURE MAP HERE - START
    feature_dim = 3     # equal to the dimension of the data
#     from qiskit.circuit import QuantumCircuit, ParameterVector

#     num_qubits = 3            
#     reps = 1              # number of times you'd want to repeat the circuit

#     x = ParameterVector('x', length=num_qubits)  # creating a list of Parameters
#     custom_circ = QuantumCircuit(num_qubits)

#     # defining our parametric form
#     for _ in range(reps):
#         for i in range(num_qubits):
#             custom_circ.rx(x[i], i)
#         for i in range(num_qubits):
#             for j in range(0, 1):
#                 custom_circ.cx(i, j)
#                 if i in {1,0} or j in {1,0}: 
#                 custom_circ.u1(x[i] * x[j], j)
#                 custom_circ.cx(i, j)

    
    # import required qiskit libraries if additional libraries are required
    
    # build the feature map
#     feature_map = ZFeatureMap(feature_dimension=feature_dim, reps=5)
    feature_map = PauliFeatureMap(feature_dimension=feature_dim,entanglement='full',reps=1, paulis = ['X','Y','XY'])
#     feature_map = ZZFeatureMap(feature_dimension=feature_dim, reps=5,entanglement='linear', insert_barriers=True)
    # BUILD FEATURE MAP HERE - END
    
    #return the feature map which is either a FeatureMap or QuantumCircuit object
    return feature_map
# the write_and_run function writes the content in this cell into the file "variational_circuit.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START

# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import  RealAmplitudes, EfficientSU2, NLocal, ExcitationPreserving

### WRITE YOUR CODE BETWEEN THESE LINES - END

def variational_circuit():
    # BUILD VARIATIONAL CIRCUIT HERE - START
    
    # import required qiskit libraries if additional libraries are required
    feature_dim = 3
    classifier_circ = RealAmplitudes(feature_dim,entanglement='linear', reps=3)
#     classifier_circ.draw()
    # build the variational circuit
    var_circuit = classifier_circ
    
    # BUILD VARIATIONAL CIRCUIT HERE - END
    
    # return the variational circuit which is either a VaritionalForm or QuantumCircuit object
    return var_circuit
# # the write_and_run function writes the content in this cell into the file "optimal_params.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def return_optimal_params():
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    
    optimal_parameters = [-2.74364902e-01,  1.82548305e+00, -1.69632700e+00,  7.39071673e-01,
       -1.11749625e+00,  1.44611066e+00,  4.90897832e-01, -1.68978218e-03,
       -2.45933934e+00,  6.45373209e-01, -7.05172097e-01,  5.63976284e-01]
    
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    return np.array(optimal_parameters)
