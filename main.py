from pyscript import document, display  # importing document and display package

# European Countries

def search(e):
    document.getElementById('display').innerHTML = " "
    nickname = document.getElementById('country').value

    display(nickname, target="display")