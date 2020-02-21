def reward_function(params):
    '''
    Student made code, first attempt at learning machine learning
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])

    # Change depending on action space setting, acts as threshold for penalty in steering
    ABS_STEERING_THRESHOLD = 20

    # Low initial reward
    reward = 1e-3

    # Reward for keeping all wheels on track, with those wheels being somewhere in between the boundaries
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Penalty to the agent for steering too much
    if steering > ABS_STEERING_THRESHOLD:
            reward *= 0.8

    return float (reward)

