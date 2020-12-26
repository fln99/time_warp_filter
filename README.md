# Time Warp Filter

The famous TikTok and Instagram filter!

### Getting Started

Change the directory to the folder where the repository content is.

Now, you may create an environment with the following python command:

```python
python -m venv env 
```

I decided to use the name 'env' for my environment, but you can put something you want.

Now, change the directory again to 'env/scripts' and type 'activate' on the terminal.

Return to the main directory address typing 'cd ..' two times, or when you see that ''env/scripts' doesn't exist on the address.

### Installing the requirements

To do this you can type on the terminal the following command:

```python
pip install -r requirements.txt
```

### Note

- This filter has the save function. The images generated will be stored into 'with_filter' folder.

- The resolution used on my tests was 640x480. So, if your webcam resolution is greater than this value, by default the program will set It to 640x480 itself.

- The default video device ID is 0, that is the first video device connected in your computer. You can change It anytime.

**This project was made on Python 3.8.5**
