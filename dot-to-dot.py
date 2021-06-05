# THIS PROGRAM IS MEANT TO BE AN INTRODUCTION TO PROGRAMMING AND TO ITS POSSIBILITES.
# ITS OBJECTIVE IS TO INTRODUCE PEOPLE TO THE THINGS WHO CAN BE DONE WITH PROGRAMMING,
# AND TO MAKE THEM UNDERSTAND THAT IT IS NOT SOME KIND OF CRYPTIC BLACK MAGIC.
# IT IS DELIBERATELY OVER-COMMENTED BECAUSE IT TARGETS BEGINNERS WHO DISCOVER IT.

# Importing the tools of selenium we need
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox() # Object used to interact with a Firefox browser
driver.get("https://play-dot-to.com/") # Go to the site
wait = WebDriverWait(driver,10) # Object used to wait some conditions to be verified

finishElement = driver.find_element_by_id("finish") # Get the victory screen
countdownElement = driver.find_element_by_id("countdown") # Get the countdown between two levels

# START SCREEN
dotsElements = driver.find_elements_by_class_name("dot")
numbersElements = driver.find_elements_by_class_name("number")
startAction = ActionChains(driver) # Object used to execute actions (click, mouse move, etc) in the browser
startAction.move_to_element(dotsElements[0]).perform() # Move the mouse to the first dot
startAction.click_and_hold(on_element=dotsElements[0]) # Click on the dot and hold the click
startAction.move_to_element(dotsElements[1]) # Move the mouse to the second click
startAction.perform() # Execute the previously described actions
startAction.reset_actions() # Clean the list of actions

# GAME
levelNum = 1 # Number of the first level
play = True
while play: # We repeat the following instructions while "play" is True
    wait.until(EC.invisibility_of_element((By.CSS_SELECTOR,"#countdown"))) # We wait until the countdown ends
    levelDotsElements = driver.find_elements_by_class_name("dot") # We get the list of the dots of the level
    nbElements = len(levelDotsElements) # Number of dots in the levels
    action= ActionChains(driver) # Object used to execute actions (click, mouse move, etc) in the browser
    action.move_to_element(levelDotsElements[0]).perform() # Move the mouse to the first dot
    action.click_and_hold(on_element=levelDotsElements[0]).perform() # Click on the dot and hold the click
    for i in range(1,nbElements+1): # For each of the other dots...
        action.move_to_element(levelDotsElements[i%nbElements]) # ...we move the mouse to it
    action.perform() # Execute the previously described actions
    action.reset_actions() # Clean the list of actions
    wait.until(EC.visibility_of(countdownElement)) # We wait until the countdown of the next level appears
    print("Level "+str(levelNum)+" complete!") # Print the recently finished level
    levelNum += 1 # Number of the new level (number of recently completed level + 1)
    if levelNum > 5:
        play = False # End of the game => we get out of the "while" loop

# VICTORY SCREEN
wait.until(EC.visibility_of(finishElement)) # Wait for the victory screen to appear
score = int(driver.find_elements_by_class_name("score")[0].get_attribute("textContent")) # Get the score
time = driver.find_elements_by_class_name("play-time")[0].get_attribute("textContent") # Get the time
print("Finish!  Score : {0}  Time : {1}".format(score,time)) # Print score and time
