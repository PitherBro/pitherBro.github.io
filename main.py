def buyFunction():
    playerCash = int(document.getElementById("cash").innerText)
    goodPrice = 5

    if playerCash >= goodPrice:
        newCash = playerCash - goodPrice
        document.getElementById("cash").innerText = str(newCash)
    else:
        alert("Not enough cash to buy the good.")

def sellFunction():
    playerCash = int(document.getElementById("cash").innerText)
    goodPrice = 10

    newCash = playerCash + goodPrice
    document.getElementById("cash").innerText = str(newCash)
