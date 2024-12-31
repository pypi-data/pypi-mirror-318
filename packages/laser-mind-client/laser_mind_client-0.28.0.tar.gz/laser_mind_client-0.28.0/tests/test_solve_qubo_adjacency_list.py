from laser_mind_client_meta import MessageKeys
from laser_mind_client import LaserMind

# Enter your TOKEN here
userToken = "<my_token>"

# Create a mock QUBO problem
quboListData = [
    [1,1,5],
    [1,2,-6],
    [2,2,3],
    [2,3,-1],
    [3,10,1]]

# Connect to the LightSolver Cloud
lsClient = LaserMind(userToken=userToken)

res = lsClient.solve_qubo(edgeList=quboListData, timeout=1)

assert MessageKeys.SOLUTION in res, "Test FAILED, response is not in expected format"

print(f"Test PASSED, response is: \n{res}")