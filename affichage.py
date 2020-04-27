from tkinter import * # Tk, Canvas, Frame, BOTH

import definition_des_pieces


class Example(Frame):

    def __init__(self, master):
        super().__init__()

        self.joueur = 0 #rouge= 0
                        #bleu = 1

        self.canvas = Canvas(self)
        self.grille()


    def changeJoeur(self, index):
        index[0]=0

        if self.joueur == 0:
            self.joueur = 1

        elif self.joueur == 1:
            self.joueur = 0



    def PieceSuivante(self, event, index, theId, canvas):
        theId[0] = inc2(index, self.joueur)
        print ("index : " , index, "theId : ", theId)

        self.efface_piece(self.canvas, theId[0], 60, 250, 1)
        self.affiche_piece(self.canvas, theId[0], 60, 250)
        
        

    def PiecePrecedente(self, event, index, theId, canvas):
        theId[0] = dec2(index, self.joueur)

        self.efface_piece(self.canvas, theId[0], 60, 250, -1)
        self.affiche_piece(self.canvas, theId[0], 60, 250)
        print ("piece actuelle :" , theId)

    def Enter(self, event, index, theId, canvas):
        print("this is Enter")

        if self.joueur==0:
            posx=370
            posy=50
        elif self.joueur==1:
            posx=970
            posy=650

        self.efface_piece(self.canvas, index[0], 60, 250, 0)
        self.affiche_piece(self.canvas, index[0], posx, posy)
        self.ChoisirLaPlaceDePieceChoisi(event, index, theId, canvas, posx, posy)


    def ChoisirLaPlaceDePieceChoisi(self, event, index, theId, canvas, posx, posy):
        canvas.bind("<Up>", lambda event, index = index, theId=theId, canvas = canvas, posx = posx, posy=posy: self.GoUp(event, index, theId, canvas, posx, posy))
        canvas.bind("<Down>", lambda event, index = index, theId=theId, canvas = canvas, posx = posx, posy=posy : self.GoDown(event, index, theId, canvas, posx, posy))
        canvas.bind("<Right>", lambda event, index = index, theId=theId, canvas = canvas, posx = posx, posy=posy : self.GoRight(event, index, theId, canvas, posx, posy))
        canvas.bind("<Left>", lambda event, index = index, theId=theId, canvas = canvas, posx = posx, posy=posy : self.GoLeft(event, index, theId, canvas, posx, posy))  
        canvas.bind("<r>", lambda event, index = index, theId=theId, canvas = canvas, posx = posx, posy=posy : self.rotatePiece(event, index, theId, canvas, posx, posy))  
        canvas.bind("<space>", lambda event, root = canvas, index = index, theId=theId : self.MettreLaPieceChoisi(event, root, index, theId))

    def MettreLaPieceChoisi(self, event, root, index, theId):
        if self.joueur==0:
            #definition_des_pieces.pieces_rouge.pop(theId[0])
            print("taille actuelle de liste rouge : ", len(definition_des_pieces.pieces_rouge))

        self.changeJoeur(index)
        self.getUserInput(root, index, theId)
        
        #elif self.joueur==1:



    def rotatePiece(self, event, index, theId, canvas, posx, posy):
        print ("rotation de la piece")
        self.efface_piece(self.canvas, index[0], posx, posy, 0)
        definition_des_pieces.pieces_rouge[index[0]].rotation()
        self.affiche_piece(self.canvas, index[0], posx, posy)
        self.grille()

    def GoUp(self, event, index, theId, canvas, posx, posy):
        print ("bouger la piece vers le haut :" , index)
        self.efface_piece(self.canvas, index[0], posx, posy, 0)
        self.affiche_piece(self.canvas, index[0], posx, posy-50)
        Example.ChoisirLaPlaceDePieceChoisi(self, event, index, theId, canvas, posx, posy-50)
        self.grille()

    def GoDown(self, event, index, theId, canvas, posx, posy):
        print ("bouger la piece vers le bas :" , index)
        self.efface_piece(self.canvas, index[0], posx, posy, 0)
        self.affiche_piece(self.canvas, index[0], posx, posy+50)
        Example.ChoisirLaPlaceDePieceChoisi(self, event, index, theId, canvas, posx, posy+50)
        self.grille()

    def GoLeft(self, event, index, theId, canvas, posx, posy):
        print ("bouger la piece vers la gauche :" , index)
        self.efface_piece(self.canvas, index[0], posx, posy, 0)
        self.affiche_piece(self.canvas, index[0], posx-50, posy)
        Example.ChoisirLaPlaceDePieceChoisi(self, event, index, theId, canvas, posx-50, posy)
        self.grille()

    def GoRight(self, event, index, theId, canvas, posx, posy):
        print ("bouger la piece vers la droit :" , index)
        self.efface_piece(self.canvas, index[0], posx, posy, 0)
        self.affiche_piece(self.canvas, index[0], posx+50, posy)
        Example.ChoisirLaPlaceDePieceChoisi(self, event, index, theId, canvas, posx+50, posy)
        self.grille()


    def key1(self, event, rootin):
        #canvas = Canvas(rootin)
        
        kp= repr(event.char)
        print ("pressed", kp)
        if event.keycode==113:
            print("let's quit")
            rootin.quit()
        """
        if event.keycode==102:
            print("what the F is pressed! La on va choisir la piece ")
            self.canvas.create_line(15, 25, 200, 25)
            #choisirPiece(event, rootin)
        """

    def affiche_piece(self, canvas, piece, pos_x, pos_y):
        if self.joueur==0:
            self.affiche_pieces_rouge(canvas, piece, pos_x, pos_y)
        else:
            self.affiche_pieces_bleu(canvas, piece, pos_x, pos_y)


    def efface_piece(self, canvas, piece, pos_x, pos_y, sense):
        if self.joueur==0:
            self.efface_pieces_rouge(canvas, piece, pos_x, pos_y, sense)
        else:
            self.efface_pieces_bleu(canvas, piece, pos_x, pos_y, sense)




    def efface_pieces_rouge(self, canvas, piece, pos_x, pos_y, sense):
        #if piece==20 and sense==-1:
           # return

        c_row = 0
        c_clm = 0

        for j in definition_des_pieces.pieces_bleu[piece-sense].forme:
            for k in j:
                if k==1:
                    canvas.create_rectangle(pos_x+c_row*50, pos_y+c_clm*50, 
                        pos_x+c_row*50+50, pos_y+c_clm*50+50,outline="white", fill="white")
                c_row=c_row+1

            c_clm=c_clm+1
            c_row = 0


    def efface_pieces_bleu(self, canvas, piece, pos_x, pos_y, sense):
        #pos_x = pos_x+1170
        #if piece==20 and sense==-1:
         #   return

        c_row = 0
        c_clm = 0

        for j in definition_des_pieces.pieces_bleu[piece-sense].forme:
            for k in j:
                if k==1:
                    canvas.create_rectangle(pos_x+c_row*50, pos_y+c_clm*50, 
                        pos_x+c_row*50+50, pos_y+c_clm*50+50,outline="white", fill="white")
                c_row=c_row+1

            c_clm=c_clm+1
            c_row = 0


    def affiche_pieces_rouge(self, canvas, piece, pos_x, pos_y):
        c_row = 0
        c_clm = 0

        for j in definition_des_pieces.pieces_rouge[piece].forme:
            for k in j:
                if k==1:
                    canvas.create_rectangle(pos_x+c_row*50, pos_y+c_clm*50, 
                        pos_x+c_row*50+50, pos_y+c_clm*50+50, fill="#E4145F")
                c_row=c_row+1

            c_clm=c_clm+1
            c_row = 0

        #print ("aff rouge OFF")

    def affiche_pieces_bleu(self, canvas, piece, pos_x, pos_y):
        #pos_x = pos_x+1170
        c_row = 0
        c_clm = 0

        for j in definition_des_pieces.pieces_bleu[piece].forme:
            for k in j:
                if k==1:
                    canvas.create_rectangle(pos_x+c_row*50, pos_y+c_clm*50, 
                        pos_x+c_row*50+50, pos_y+c_clm*50+50, fill="#2198F5")
                c_row=c_row+1

            c_clm=c_clm+1
            c_row = 0


    def grille(self):
        
        #self.configure(background='black')

        self.pack(fill=BOTH, expand=1)

        #canvas = Canvas(self)

        for i in range(15):
            self.canvas.create_line(i*50+370, 50, i*50+370, 750)

        for i in range(15):
            self.canvas.create_line(370, i*50+50, 1070, i*50+50)


        self.canvas.pack(fill=BOTH, expand=1)


    def getUserInput(self, root, index, theId):
        print ("we restart taking users input")

        

        root.unbind("<Left>")
        root.unbind("<Right>")

        root.bind("<Key>", lambda event, canvas = root : self.key1(event, canvas))

        root.bind("<Up>", lambda event, index = index, theId= theId, canvas = root : self.PieceSuivante(event, index, theId, canvas))
        root.bind("<Down>", lambda event, index = index, theId= theId, canvas = root : self.PiecePrecedente(event, index, theId, canvas))

        root.bind("<Return>", lambda event, index = index, theId=theId, canvas = root: self.Enter(event, index, theId, canvas))



"""
def inc(n):
    if n[0]==20: #len(definition_des_pieces.all_pieces.joueur)-1
        n[0]=0      # return 0
    else:
        n[0]+=1
"""

def inc2(n, joueur):
    if n[0]==len(definition_des_pieces.all_pieces[joueur])-1:
        n[0]=0
        return 0
    else:
        #tmp = n[0]
        n[0]+=1
        return definition_des_pieces.all_pieces[joueur][n[0]].id


def dec(n):
    if n[0]==0:
        n[0]=20
    else:
        n[0]-=1


def dec2(n, joueur):
    if n[0]==0:
        n[0]=len(definition_des_pieces.all_pieces[joueur])-1
        return definition_des_pieces.all_pieces[joueur][len(definition_des_pieces.all_pieces[joueur])-1].id
    else:
        #tmp = n[0]
        n[0]-=1
        return definition_des_pieces.all_pieces[joueur][n[0]].id



def main():

    """
    for i in definition_des_pieces.all_pieces:
        for j in range (21):
            print (i[j].id)
    """

    index=[0]
    indexBleu=[0]
    theId=[0]

    positionInitialeGrille=[370, 50]

    root = Tk()
    root.title('BLOCUS')
    root.geometry("1440x860")


    ex = Example(root)

    ex.getUserInput(root, index, theId)      #, positionInitialeGrille)
    root.mainloop()


if __name__ == '__main__':
    main()


