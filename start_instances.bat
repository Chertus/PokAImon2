@echo off
cd C:\Users\Administrator\Documents\Projects\PokemonRedExperiments-master\baselines
for /l %%i in (1,1,10) do (
    start python run_pretrained_interactive.py
)
