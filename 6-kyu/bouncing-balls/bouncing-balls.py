def bouncing_ball(h, bounce, window):
    # your code
    if h > 0 and 0 < bounce < 1 and window < h:
        ball_pass_the_mom_count = -1
        
        while window < h:
            ball_pass_the_mom_count += 2           
            h *= bounce
        
        return ball_pass_the_mom_count
    return -1