#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on September 15, 2023, at 23:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'IOWA_Gambling_4Choice_H'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'age': '',
    'sex': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=' /Users/baoquynh/Downloads/iowa_gambling_4choice_h-master',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "Instructions1" ---
Instruct1_text = visual.TextStim(win=win, name='Instruct1_text',
    text='In this game, you will see a series of cards. You must choose a card to PLAY\n\nSometimes you will win money, sometimes you will lose money.  \n\nYour job is to try to win as much money as possible.\n\nPress spacebar to continue. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instruct1_Resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from MoneyList_code
Block = 0
CardChoice = 0
CardChoice_code = 0
GoodDeck = 3
CardAcc = 3
CardCounter = 0
KnowledgeCounter = 0
CardList = [0]
MoneyList = [0]
KnowList = [0]
CurrentKnow = 0

A_Counter = 0
A_moneyCounter = 0
B_Counter = 0
B_moneyCounter = 0
C_Counter = 0
C_moneyCounter = 0
D_Counter = 0
D_moneyCounter = 0
MoneyCounter = 0

Bank = 2000

ChoiceStartTime = 0
ChoiceTimePassed = 0
ChoiceTimedOut = 0

FeedbackCoords = 0
MsgColor = 'black'
PlusMinus = ' '
Msg = ' '

KnowInstrct2_Rep = 1

imgA = 'card_choice.png'
imgB = 'card_choice.png'
imgC = 'card_choice.png'
imgD = 'card_choice.png'

# --- Initialize components for Routine "Instructions2" ---
Instruct2_text = visual.TextStim(win=win, name='Instruct2_text',
    text='You will start with €2000 in the bank\n\nThere are good decks and bad decks in this game.  You can win the most money by learning to avoid the bad decks and selecting cards only from the good decks.\n\nWe cannot tell you which decks are good and bad.\n\nPress spacebar to continue.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instruct2_Resp = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions3" ---
A0 = visual.ImageStim(
    win=win,
    name='A0', 
    image='card_choice.png', mask=None, anchor='center',
    ori=0, pos=(-.36, .1), size=[.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
B0 = visual.ImageStim(
    win=win,
    name='B0', 
    image='card_choice.png', mask=None, anchor='center',
    ori=0, pos=(-.12, .1), size=[.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
C0 = visual.ImageStim(
    win=win,
    name='C0', 
    image='card_choice.png', mask=None, anchor='center',
    ori=0, pos=(.12, .1), size=[.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
D0 = visual.ImageStim(
    win=win,
    name='D0', 
    image='card_choice.png', mask=None, anchor='center',
    ori=0, pos=(.36, .1), size=[.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Instruct3_Resp = keyboard.Keyboard()
Instruct3_text = visual.TextStim(win=win, name='Instruct3_text',
    text='This is what the screen will look like. \n\nYou can choose a card by selecting either 1, 2, 3 or 4 on the keyboard\n\nPress spacebar to begin.',
    font='Arial',
    pos=(0, -.25), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Bank" ---
Banktext = visual.TextStim(win=win, name='Banktext',
    text='Your Current Total:  €' + str(Bank),
    font='Arial',
    pos=(0, .1), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Initializing_text = visual.TextStim(win=win, name='Initializing_text',
    text='Intializing...',
    font='Arial',
    pos=(0, -.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Choice" ---
ChoiceResp = keyboard.Keyboard()
A = visual.ImageStim(
    win=win,
    name='A', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
B = visual.ImageStim(
    win=win,
    name='B', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
C = visual.ImageStim(
    win=win,
    name='C', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
D = visual.ImageStim(
    win=win,
    name='D', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text = visual.TextStim(win=win, name='text',
    text='1',
    font='Arial',
    pos=(-.36, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='2',
    font='Arial',
    pos=(-.12, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='3',
    font='Arial',
    pos=(.12, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='4',
    font='Arial',
    pos=(.36, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "ProcessChoice" ---

# --- Initialize components for Routine "SetMoney" ---

# --- Initialize components for Routine "Feedback" ---
A2 = visual.ImageStim(
    win=win,
    name='A2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
B2 = visual.ImageStim(
    win=win,
    name='B2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
C2 = visual.ImageStim(
    win=win,
    name='C2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
D2 = visual.ImageStim(
    win=win,
    name='D2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
DisplayCurrentMoney_1 = visual.TextStim(win=win, name='DisplayCurrentMoney_1',
    text='',
    font='Arial',
    pos=[0,-.2], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Message = visual.TextStim(win=win, name='Message',
    text='',
    font='Arial',
    pos=(0, -.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Bank_text = visual.TextStim(win=win, name='Bank_text',
    text='',
    font='Arial',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='4',
    font='Arial',
    pos=(.36, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='1',
    font='Arial',
    pos=(-.36, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='3',
    font='Arial',
    pos=(.12, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='2',
    font='Arial',
    pos=(-.12, .3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# --- Initialize components for Routine "End" ---
thank_you = visual.TextStim(win=win, name='thank_you',
    text='This is the end of the experiment.\nThank you for your time.\n\nPress spacebar to close.',
    font='Arial',
    pos=(0, 0-.15), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Bank_text_2 = visual.TextStim(win=win, name='Bank_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Instruct1_Resp.keys = []
Instruct1_Resp.rt = []
_Instruct1_Resp_allKeys = []
# keep track of which components have finished
Instructions1Components = [Instruct1_text, Instruct1_Resp]
for thisComponent in Instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct1_text* updates
    if Instruct1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct1_text.frameNStart = frameN  # exact frame index
        Instruct1_text.tStart = t  # local t and not account for scr refresh
        Instruct1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct1_text, 'tStartRefresh')  # time at next scr refresh
        Instruct1_text.setAutoDraw(True)
    
    # *Instruct1_Resp* updates
    waitOnFlip = False
    if Instruct1_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct1_Resp.frameNStart = frameN  # exact frame index
        Instruct1_Resp.tStart = t  # local t and not account for scr refresh
        Instruct1_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct1_Resp, 'tStartRefresh')  # time at next scr refresh
        Instruct1_Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instruct1_Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instruct1_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instruct1_Resp.status == STARTED and not waitOnFlip:
        theseKeys = Instruct1_Resp.getKeys(keyList=['space'], waitRelease=False)
        _Instruct1_Resp_allKeys.extend(theseKeys)
        if len(_Instruct1_Resp_allKeys):
            Instruct1_Resp.keys = _Instruct1_Resp_allKeys[-1].name  # just the last key pressed
            Instruct1_Resp.rt = _Instruct1_Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions1" ---
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instruct1_Resp.keys in ['', [], None]:  # No response was made
    Instruct1_Resp.keys = None
thisExp.addData('Instruct1_Resp.keys',Instruct1_Resp.keys)
if Instruct1_Resp.keys != None:  # we had a response
    thisExp.addData('Instruct1_Resp.rt', Instruct1_Resp.rt)
thisExp.nextEntry()
# Run 'End Routine' code from MoneyList_code
Block = 1
# the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Instruct2_Resp.keys = []
Instruct2_Resp.rt = []
_Instruct2_Resp_allKeys = []
# keep track of which components have finished
Instructions2Components = [Instruct2_text, Instruct2_Resp]
for thisComponent in Instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct2_text* updates
    if Instruct2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct2_text.frameNStart = frameN  # exact frame index
        Instruct2_text.tStart = t  # local t and not account for scr refresh
        Instruct2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct2_text, 'tStartRefresh')  # time at next scr refresh
        Instruct2_text.setAutoDraw(True)
    
    # *Instruct2_Resp* updates
    waitOnFlip = False
    if Instruct2_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct2_Resp.frameNStart = frameN  # exact frame index
        Instruct2_Resp.tStart = t  # local t and not account for scr refresh
        Instruct2_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct2_Resp, 'tStartRefresh')  # time at next scr refresh
        Instruct2_Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instruct2_Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instruct2_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instruct2_Resp.status == STARTED and not waitOnFlip:
        theseKeys = Instruct2_Resp.getKeys(keyList=['space'], waitRelease=False)
        _Instruct2_Resp_allKeys.extend(theseKeys)
        if len(_Instruct2_Resp_allKeys):
            Instruct2_Resp.keys = _Instruct2_Resp_allKeys[-1].name  # just the last key pressed
            Instruct2_Resp.rt = _Instruct2_Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions2" ---
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Instruct3_Resp.keys = []
Instruct3_Resp.rt = []
_Instruct3_Resp_allKeys = []
# keep track of which components have finished
Instructions3Components = [A0, B0, C0, D0, Instruct3_Resp, Instruct3_text]
for thisComponent in Instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *A0* updates
    if A0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        A0.frameNStart = frameN  # exact frame index
        A0.tStart = t  # local t and not account for scr refresh
        A0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(A0, 'tStartRefresh')  # time at next scr refresh
        A0.setAutoDraw(True)
    
    # *B0* updates
    if B0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        B0.frameNStart = frameN  # exact frame index
        B0.tStart = t  # local t and not account for scr refresh
        B0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(B0, 'tStartRefresh')  # time at next scr refresh
        B0.setAutoDraw(True)
    
    # *C0* updates
    if C0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        C0.frameNStart = frameN  # exact frame index
        C0.tStart = t  # local t and not account for scr refresh
        C0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C0, 'tStartRefresh')  # time at next scr refresh
        C0.setAutoDraw(True)
    
    # *D0* updates
    if D0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        D0.frameNStart = frameN  # exact frame index
        D0.tStart = t  # local t and not account for scr refresh
        D0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(D0, 'tStartRefresh')  # time at next scr refresh
        D0.setAutoDraw(True)
    
    # *Instruct3_Resp* updates
    waitOnFlip = False
    if Instruct3_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct3_Resp.frameNStart = frameN  # exact frame index
        Instruct3_Resp.tStart = t  # local t and not account for scr refresh
        Instruct3_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct3_Resp, 'tStartRefresh')  # time at next scr refresh
        Instruct3_Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instruct3_Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instruct3_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instruct3_Resp.status == STARTED and not waitOnFlip:
        theseKeys = Instruct3_Resp.getKeys(keyList=['space'], waitRelease=False)
        _Instruct3_Resp_allKeys.extend(theseKeys)
        if len(_Instruct3_Resp_allKeys):
            Instruct3_Resp.keys = _Instruct3_Resp_allKeys[-1].name  # just the last key pressed
            Instruct3_Resp.rt = _Instruct3_Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Instruct3_text* updates
    if Instruct3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct3_text.frameNStart = frameN  # exact frame index
        Instruct3_text.tStart = t  # local t and not account for scr refresh
        Instruct3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct3_text, 'tStartRefresh')  # time at next scr refresh
        Instruct3_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions3" ---
for thisComponent in Instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Bank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
BankComponents = [Banktext, Initializing_text]
for thisComponent in BankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Bank" ---
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Banktext* updates
    if Banktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Banktext.frameNStart = frameN  # exact frame index
        Banktext.tStart = t  # local t and not account for scr refresh
        Banktext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Banktext, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Banktext.started')
        Banktext.setAutoDraw(True)
    if Banktext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Banktext.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            Banktext.tStop = t  # not accounting for scr refresh
            Banktext.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Banktext.stopped')
            Banktext.setAutoDraw(False)
    
    # *Initializing_text* updates
    if Initializing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Initializing_text.frameNStart = frameN  # exact frame index
        Initializing_text.tStart = t  # local t and not account for scr refresh
        Initializing_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Initializing_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Initializing_text.started')
        Initializing_text.setAutoDraw(True)
    if Initializing_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Initializing_text.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            Initializing_text.tStop = t  # not accounting for scr refresh
            Initializing_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Initializing_text.stopped')
            Initializing_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Bank" ---
for thisComponent in BankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# set up handler to look after randomisation of conditions etc
ChoiceBlock = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('GainLosConds_testforshortexp.xlsx'),
    seed=None, name='ChoiceBlock')
thisExp.addLoop(ChoiceBlock)  # add the loop to the experiment
thisChoiceBlock = ChoiceBlock.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChoiceBlock.rgb)
if thisChoiceBlock != None:
    for paramName in thisChoiceBlock:
        exec('{} = thisChoiceBlock[paramName]'.format(paramName))

for thisChoiceBlock in ChoiceBlock:
    currentLoop = ChoiceBlock
    # abbreviate parameter names if possible (e.g. rgb = thisChoiceBlock.rgb)
    if thisChoiceBlock != None:
        for paramName in thisChoiceBlock:
            exec('{} = thisChoiceBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Choice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ChoiceTime_code
    ChoiceStartTime = globalClock.getTime()
    ChoiceTimePassed = 0
    ChoiceTimedOut = 0
    CardChoice = 0
    CurrentCard = ''
    Outcome = 0;
    
    imgA = 'card_choice.png'
    imgB = 'card_choice.png'
    imgC = 'card_choice.png'
    imgD = 'card_choice.png'
    ChoiceResp.keys = []
    ChoiceResp.rt = []
    _ChoiceResp_allKeys = []
    A.setPos((-.36, .1))
    A.setSize([.3])
    A.setImage(imgA)
    B.setPos((-.12, .1))
    B.setSize([.3])
    B.setImage(imgB)
    C.setPos((.12, .1))
    C.setSize([.3])
    C.setImage(imgC)
    D.setPos((.36, .1))
    D.setSize([.3])
    D.setImage(imgD)
    # keep track of which components have finished
    ChoiceComponents = [ChoiceResp, A, B, C, D, text, text_2, text_3, text_4, text_6]
    for thisComponent in ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Choice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from ChoiceTime_code
        ChoiceTimePassed = (globalClock.getTime() - ChoiceStartTime)
        choiceStr = 'XXXXXX'
        
        
        # *ChoiceResp* updates
        waitOnFlip = False
        if ChoiceResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ChoiceResp.frameNStart = frameN  # exact frame index
            ChoiceResp.tStart = t  # local t and not account for scr refresh
            ChoiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ChoiceResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ChoiceResp.started')
            ChoiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ChoiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ChoiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ChoiceResp.status == STARTED and not waitOnFlip:
            theseKeys = ChoiceResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _ChoiceResp_allKeys.extend(theseKeys)
            if len(_ChoiceResp_allKeys):
                ChoiceResp.keys = _ChoiceResp_allKeys[-1].name  # just the last key pressed
                ChoiceResp.rt = _ChoiceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *A* updates
        if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A.frameNStart = frameN  # exact frame index
            A.tStart = t  # local t and not account for scr refresh
            A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
            A.setAutoDraw(True)
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            B.setAutoDraw(True)
        
        # *C* updates
        if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C.frameNStart = frameN  # exact frame index
            C.tStart = t  # local t and not account for scr refresh
            C.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
            C.setAutoDraw(True)
        
        # *D* updates
        if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D.frameNStart = frameN  # exact frame index
            D.tStart = t  # local t and not account for scr refresh
            D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
            D.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            text_4.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:  # only update if drawing
            text_6.setPos((0,-.25), log=False)
            text_6.setText('SELECT A CARD', log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Choice" ---
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from ChoiceTime_code
    if(ChoiceResp.keys == '1'):
        CurrentCard = 'A_Card'
    elif(ChoiceResp.keys == '2'):
        CurrentCard = 'B_Card'
    elif(ChoiceResp.keys == '3'):
        CurrentCard = 'C_Card'
    elif(ChoiceResp.keys == '4'):
        CurrentCard = 'D_Card'
    # check responses
    if ChoiceResp.keys in ['', [], None]:  # No response was made
        ChoiceResp.keys = None
    ChoiceBlock.addData('ChoiceResp.keys',ChoiceResp.keys)
    if ChoiceResp.keys != None:  # we had a response
        ChoiceBlock.addData('ChoiceResp.rt', ChoiceResp.rt)
    # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ProcessChoice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ProcessChoice_code
    if(ChoiceResp.keys == '1'):
        A_Counter = A_Counter + 1
        A_moneyCounter = (A_Counter - 1)
        A_Counter = A_Counter + 1
        GoodDeck = 0
        CardAcc = 0
        Outcome = A_Outcome
        print(Outcome)
    elif(ChoiceResp.keys == '2'):
        B_Counter = B_Counter + 1
        B_moneyCounter = (B_Counter - 1)
        GoodDeck = 0
        CardAcc = 0
        Outcome = B_Outcome
    elif(ChoiceResp.keys == '3'):
        C_Counter = C_Counter + 1
        C_moneyCounter = (C_Counter - 1)
        GoodDeck = 1
        CardAcc = 1
        Outcome = C_Outcome
    elif(ChoiceResp.keys == '4'):
        D_Counter = D_Counter + 1
        D_moneyCounter = (D_Counter - 1)
        GoodDeck = 1
        CardAcc = 1
        Outcome = D_Outcome
    # keep track of which components have finished
    ProcessChoiceComponents = []
    for thisComponent in ProcessChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ProcessChoice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ProcessChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ProcessChoice" ---
    for thisComponent in ProcessChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from ProcessChoice_code
    print(Outcome)
    print(type(Bank))
    print(type(Outcome))
    Bank = Bank + Outcome
    # the Routine "ProcessChoice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "SetMoney" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    SetMoneyComponents = []
    for thisComponent in SetMoneyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SetMoney" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SetMoneyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SetMoney" ---
    for thisComponent in SetMoneyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from SetCurrentMoney
    if (Outcome > 0):
        PlusMinus = ('+ €')
        MsgColor = 'green'
        Msg = 'YOU WON!!!'
        DisplayMoney=abs(Outcome)
    elif (Outcome < 0):
        MsgColor = 'red'
        PlusMinus = ('- €')
        Msg = 'YOU LOSE!!!'
        DisplayMoney=abs(Outcome)
    # the Routine "SetMoney" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CardCounter_code
    if(ChoiceResp.keys == '1'):
        CurrentCard = 'A_Card'
        choiceStr = '1'
        imgA = 'card_selected.png'
        imgB = 'card_choice.png'
        imgC = 'card_choice.png'
        imgD = 'card_choice.png'
    elif(ChoiceResp.keys == '2'):
        CurrentCard = 'B_Card'
        choiceStr = '2'
        imgB = 'card_selected.png'
        imgA = 'card_choice.png'
        imgC = 'card_choice.png'
        imgD = 'card_choice.png'
    elif(ChoiceResp.keys == '3'):
        imgC = 'card_selected.png'
        choiceStr = '3'
        imgB = 'card_choice.png'
        imgA = 'card_choice.png'
        imgD = 'card_choice.png'
        CurrentCard = 'C_Card'
    elif(ChoiceResp.keys == '4'):
        CurrentCard = 'D_Card'
        imgD = 'card_selected.png'
        choiceStr = '4'
        imgB = 'card_choice.png'
        imgC = 'card_choice.png'
        imgA = 'card_choice.png'
    A2.setPos((-.36, .1))
    A2.setSize([.3])
    A2.setImage(imgA)
    B2.setPos((-.12, .1))
    B2.setSize([.3])
    B2.setImage(imgB)
    C2.setPos((.12, .1))
    C2.setSize([.3])
    C2.setImage(imgC)
    D2.setPos((.36, .1))
    D2.setSize([.3])
    D2.setImage(imgD)
    DisplayCurrentMoney_1.setColor(MsgColor, colorSpace='rgb')
    DisplayCurrentMoney_1.setText(''+ str(PlusMinus) + str(DisplayMoney))
    Message.setText(str(Msg) )
    Bank_text.setText('Your Current Total: ' + '€' + str(Bank))
    # keep track of which components have finished
    FeedbackComponents = [A2, B2, C2, D2, DisplayCurrentMoney_1, Message, Bank_text, text_9, text_5, text_8, text_7]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Feedback" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A2* updates
        if A2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A2.frameNStart = frameN  # exact frame index
            A2.tStart = t  # local t and not account for scr refresh
            A2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A2, 'tStartRefresh')  # time at next scr refresh
            A2.setAutoDraw(True)
        if A2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > A2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                A2.tStop = t  # not accounting for scr refresh
                A2.frameNStop = frameN  # exact frame index
                A2.setAutoDraw(False)
        
        # *B2* updates
        if B2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B2.frameNStart = frameN  # exact frame index
            B2.tStart = t  # local t and not account for scr refresh
            B2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B2, 'tStartRefresh')  # time at next scr refresh
            B2.setAutoDraw(True)
        if B2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                B2.tStop = t  # not accounting for scr refresh
                B2.frameNStop = frameN  # exact frame index
                B2.setAutoDraw(False)
        
        # *C2* updates
        if C2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C2.frameNStart = frameN  # exact frame index
            C2.tStart = t  # local t and not account for scr refresh
            C2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C2, 'tStartRefresh')  # time at next scr refresh
            C2.setAutoDraw(True)
        if C2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                C2.tStop = t  # not accounting for scr refresh
                C2.frameNStop = frameN  # exact frame index
                C2.setAutoDraw(False)
        
        # *D2* updates
        if D2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D2.frameNStart = frameN  # exact frame index
            D2.tStart = t  # local t and not account for scr refresh
            D2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D2, 'tStartRefresh')  # time at next scr refresh
            D2.setAutoDraw(True)
        if D2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > D2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                D2.tStop = t  # not accounting for scr refresh
                D2.frameNStop = frameN  # exact frame index
                D2.setAutoDraw(False)
        
        # *DisplayCurrentMoney_1* updates
        if DisplayCurrentMoney_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            DisplayCurrentMoney_1.frameNStart = frameN  # exact frame index
            DisplayCurrentMoney_1.tStart = t  # local t and not account for scr refresh
            DisplayCurrentMoney_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DisplayCurrentMoney_1, 'tStartRefresh')  # time at next scr refresh
            DisplayCurrentMoney_1.setAutoDraw(True)
        if DisplayCurrentMoney_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DisplayCurrentMoney_1.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                DisplayCurrentMoney_1.tStop = t  # not accounting for scr refresh
                DisplayCurrentMoney_1.frameNStop = frameN  # exact frame index
                DisplayCurrentMoney_1.setAutoDraw(False)
        
        # *Message* updates
        if Message.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Message.frameNStart = frameN  # exact frame index
            Message.tStart = t  # local t and not account for scr refresh
            Message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Message, 'tStartRefresh')  # time at next scr refresh
            Message.setAutoDraw(True)
        if Message.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Message.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Message.tStop = t  # not accounting for scr refresh
                Message.frameNStop = frameN  # exact frame index
                Message.setAutoDraw(False)
        
        # *Bank_text* updates
        if Bank_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Bank_text.frameNStart = frameN  # exact frame index
            Bank_text.tStart = t  # local t and not account for scr refresh
            Bank_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bank_text, 'tStartRefresh')  # time at next scr refresh
            Bank_text.setAutoDraw(True)
        if Bank_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bank_text.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Bank_text.tStop = t  # not accounting for scr refresh
                Bank_text.frameNStop = frameN  # exact frame index
                Bank_text.setAutoDraw(False)
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_9.started')
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.stopped')
                text_9.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                text_5.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.stopped')
                text_8.setAutoDraw(False)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback" ---
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from CardCounter_code
    CardCounter = CardCounter + 1
    ChoiceBlock.addData('Chosen_Card', CurrentCard)
    ChoiceBlock.addData('GoodDeck?', GoodDeck)
    ChoiceBlock.addData('GainsLosses', Outcome)
    ChoiceBlock.addData('TotalinBank', Bank)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1 repeats of 'ChoiceBlock'

# get names of stimulus parameters
if ChoiceBlock.trialList in ([], [None], None):
    params = []
else:
    params = ChoiceBlock.trialList[0].keys()
# save data for this loop
ChoiceBlock.saveAsExcel(filename + '.xlsx', sheetName='ChoiceBlock',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Bank_text_2.setText('Your Final Total: ' + '€' + str(Bank))
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
EndComponents = [thank_you, Bank_text_2, key_resp]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank_you.started')
        thank_you.setAutoDraw(True)
    
    # *Bank_text_2* updates
    if Bank_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Bank_text_2.frameNStart = frameN  # exact frame index
        Bank_text_2.tStart = t  # local t and not account for scr refresh
        Bank_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Bank_text_2, 'tStartRefresh')  # time at next scr refresh
        Bank_text_2.setAutoDraw(True)
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
