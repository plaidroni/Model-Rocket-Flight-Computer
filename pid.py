import numpy
from pylab import * 


delT = 1.0 / 98.0 # time step is 98Hz, per spec sheet of arduino nano
Inertia = 0.0202 #TODO: Get a better estimate of the inertia
#we can either do some simple interial calculations, with I = 1/12m(3r^2 + L^2) for a rod,
#or we can do a more accurate calculation by modeling the rocket as a collection of point masses and summing m*r^2 for each mass.

numSamples = 350   #total runtime = delT*numSamples
d = 0.215     #distance between engine and Cg
Force = 15  #Estes F15
theta0 = -0*pi/180.  #setpoint
Kp = 45 #the further we are from our target, the harder we should try to correct
Ki = 0.2 #the longer we have been away from our target, the harder we should try to correct 
Kd = 10 #if we're quickly getting close to where you want we be, slow down.
theta = numpy.zeros( numSamples)
t = [x*delT for x in range(numSamples)]
torque = numpy.zeros( numSamples )
setpoint = numpy.zeros( numSamples )
time_thrust_samples = numpy.array([
		0.00, 0.23, 0.34, 0.39, 0.43, 0.48, 0.58, 1.19, 1.57, 2.00, 2.68, 3.35, 3.40
	]) # thanks https://www.rocketreviews.com/e-f15.html!
force_thrust_samples = numpy.array([
		0.00, 4.407, 20.82, 26.75, 25.38, 22.19, 17.93, 14.59, 15.65, 14.28, 13.08, 13.00, 0.00
	])


#in degrees
maxangle = 5.5  
maxRotationPerStep = 20/0.1*delT  #100mS/60deg per spec sheet, this is hte max change in servo angle per step

# from data pulled from https://www.rocketreviews.com/e-f15.html
#(static fires are too expensive :P)
def getForce(t):
	# Smooth thrust curve (Estes F15 sample points, time in seconds, thrust in Newtons)
	

	# Outside the data range: no thrust
	if t <= time_thrust_samples[0] or t >= time_thrust_samples[-1]:
		return 0.0

	# Find interval index i such that time_thrust_samples[i] <= t < time_thrust_samples[i+1]
	i = numpy.searchsorted(time_thrust_samples, t, side="right") - 1
	# Normalize time within the interval
		
	# Smoothstep interpolation for a continuous, smooth curve
	t0, t1 = time_thrust_samples[i], time_thrust_samples[i + 1]
	f0, f1 = force_thrust_samples[i], force_thrust_samples[i + 1]
	u = (t - t0) / (t1 - t0)
	s = u * u * (3.0 - 2.0 * u)  # smoothstep: C1-continuous
	return f0 + (f1 - f0) * s
		
	
	
	
# intial conditions
initialTh = -10
theta[0] = initialTh*pi/180.   #must be in radians
theta[1] = initialTh*pi/180.   #deg
runningSum = theta[0]+theta[1]
for n in range(2, numSamples):

	torque[n-1] = d*getForce(n*delT)*sin( pi*setpoint[n-1]/180.)

	theta[n] = 2*theta[n-1] - theta[n-2] + torque[n-2]*delT*delT/Inertia #+ 0.0005*numpy.random.standard_normal()
	
	#PID control
	runningSum = runningSum + (theta[n]-theta0)


	desiredSetpoint = - Kp*(theta[n]-theta0) - Kd*(theta[n]-theta[n-1])/delT - Ki*runningSum
	if( (desiredSetpoint - setpoint[n-1])>maxRotationPerStep ):
		setpoint[n] = setpoint[n-1] + maxRotationPerStep
	elif( (setpoint[n-1]-desiredSetpoint)>maxRotationPerStep ):
		setpoint[n] = setpoint[n-1] - maxRotationPerStep
	else:
		setpoint[n] = desiredSetpoint
		 
	if( setpoint[n] > maxangle ):
		setpoint[n] = maxangle
	if( setpoint[n] <-maxangle ):
		setpoint[n] = -maxangle
		
	print "n=" + str(n) + " theta=" + str(theta[n]) + " setpoint=" + str(setpoint[n])
	

print maxRotationPerStep
p = plot(t, 180/pi*theta, 'k')
grid()
plot(t, setpoint, 'b')	
xlabel('time [s]')
plt.show()
