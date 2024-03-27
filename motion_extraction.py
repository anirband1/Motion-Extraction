import cv2

FRAME_DELAY = 5

cam = cv2.VideoCapture(0)
frames = []

while True:
    ret, fr = cam.read()
    frames.append(fr)

    if len(frames) > FRAME_DELAY:
        frames = frames[len(frames) - FRAME_DELAY:]

    fr_inv = frames[0]

    fr_inv = 255-fr_inv

    # final_fr = (frames[-1] + fr_inv)/2
      
    final_fr = cv2.addWeighted(frames[-1], 0.5, fr_inv, 0.5, 1)

    final_fr = cv2.flip(final_fr, 1)
    cv2.imshow("Motion Extraction", final_fr)

    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break

cam.release()
cv2.destroyAllWindows()