# Hides Streamlit's excessive UI - brings page content up
remove_st_ui = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
</style>
"""

# Removes the anchors next to titles
no_anchors = """""" # Broken right now =(

# Removes the user settings menu
hide_settings = """
<style>div[data-testid="stToolbar"] { display: none;}</style>
"""

# Hides the 'made with streamlit' message when hosting
hide_made_with_s = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """



# Hides the text: 'press enter to submit' on forms, even though the function is still active
hide_enter_to_submit = """
    <style>
    [data-testid="InputInstructions"] { display:None }
    </style>
    """

# Remove the header
remove_header = """
            <style>
            header {visibility: hidden;}
            </style>
            """

# Hides the orange/red/yellow bar at the top
# BROKEN =(
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''