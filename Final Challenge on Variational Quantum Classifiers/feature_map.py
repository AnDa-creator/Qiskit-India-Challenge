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
#     feature_map = PauliFeatureMap(feature_dimension=feature_dim,entanglement='full',reps=1, paulis = ['X','Y','XY'])
    feature_map = ZZFeatureMap(feature_dimension=feature_dim, reps=10,entanglement='linear', insert_barriers=True)
    # BUILD FEATURE MAP HERE - END
    
    #return the feature map which is either a FeatureMap or QuantumCircuit object
    return feature_map
