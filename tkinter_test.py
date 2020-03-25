from tkinter import * # Tk, Canvas, Frame, BOTH

import definition_des_pieces

class Example(Frame):

    def __init__(self, master):
        super().__init__()

        self.initUI()



    def affiche_pieces_rouge(self, canvas, piece, pos_x, pos_y):
    	c_row = 0
    	c_clm = 0

    	for j in piece.forme:
    		for k in j:
    			if k==1:
    				canvas.create_rectangle(pos_x+c_row*50+5, pos_y+c_clm*50, 
    					pos_x+c_row*50+50+5, pos_y+c_clm*50+50, fill="#E4145F")
    			c_row=c_row+1

    		c_clm=c_clm+1
    		c_row = 0


    def affiche_pieces_bleu(self, canvas, piece, pos_x, pos_y):
   		pos_x = pos_x+1070
   		c_row = 0
   		c_clm = 0

   		for j in piece.forme:
   			if piece.id != 9:
	   			for k in j:
	   				if k==1:
	   					canvas.create_rectangle(pos_x+c_row*50+5, pos_y+c_clm*50, 
	    					pos_x+c_row*50+50+5, pos_y+c_clm*50+50, fill="#2198F5")
	   				c_row=c_row+1
	   			c_clm=c_clm+1
	   			c_row = 0
	   		else:
	   			pos_x = 930
	   			for k in j:
	   				if k==1:
	   					canvas.create_rectangle(pos_x+c_row*50+5, pos_y+c_clm*50, 
	    					pos_x+c_row*50+50+5, pos_y+c_clm*50+50, fill="#2198F5")
	   				c_row=c_row+1
	   			c_clm=c_clm+1
	   			c_row = 0


    def initUI(self):
        
        self.configure(background='black')

        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        


        for i in range(15):
            canvas.create_line(i*50+370, 00, i*50+370, 700)

        for i in range(15):
            canvas.create_line(370, i*50, 1070, i*50)




        for i in definition_des_pieces.pieces_rouge:

        	if i.id==0:
        		self.affiche_pieces_rouge(canvas, i, 20, 745)		# done

        	if i.id==1:
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 290, 470)		# done

        	if i.id==2:
        		self.affiche_pieces_rouge(canvas, i, 120, 117)		# done

        	if i.id==3:
        		self.affiche_pieces_rouge(canvas, i, 120, 235)		# done

        	if i.id==4:
        		self.affiche_pieces_rouge(canvas, i, 155, 10)		# 111111111

        	if i.id==5:
        		i.rotation()
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 10, 70)		# done

        	if i.id==6:
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 240, 240)		#  done

        	if i.id==7:
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 125, 355)		# done

        	if i.id==8:
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 5, 240)		# done

        	if i.id==9:
        		self.affiche_pieces_rouge(canvas, i, 340, 703)		# done

        	if i.id==10:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 210, 15)		# done 	// ........

        	if i.id==11:
        		self.affiche_pieces_rouge(canvas, i, 0, 5)			# done	

        	if i.id==12:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 75, 460)		# done

        	if i.id==13:
        		self.affiche_pieces_rouge(canvas, i, 180, 415)		# done	


        	if i.id==14:
        		self.affiche_pieces_rouge(canvas, i, 17, 350)		# done


        	if i.id==15:
        		self.affiche_pieces_rouge(canvas, i, 180, 120)		# done


        	if i.id==16:
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 10, 480)		# done

        	if i.id==17:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 160, 575)		# done

        	if i.id==18:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 130, 630)		# done

        		

        	elif i.id==19:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_rouge(canvas, i, 20, 640)


        	elif i.id==20:
        		self.affiche_pieces_rouge(canvas, i, 80, 745)




        for i in definition_des_pieces.pieces_bleu:

        	if i.id==0:
        		self.affiche_pieces_bleu(canvas, i, 20, 745)		# done

        	if i.id==1:
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 290, 470)		# done

        	if i.id==2:
        		self.affiche_pieces_bleu(canvas, i, 120, 117)		# done

        	if i.id==3:
        		self.affiche_pieces_bleu(canvas, i, 120, 235)		# done

        	if i.id==4:
        		self.affiche_pieces_bleu(canvas, i, 155, 10)		# 111111111

        	if i.id==5:
        		i.rotation()
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 10, 70)		# done

        	if i.id==6:
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 240, 240)		#  done

        	if i.id==7:
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 125, 355)		# done

        	if i.id==8:
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 5, 240)		# done

        	if i.id==9:
        		self.affiche_pieces_bleu(canvas, i, 340, 703)		# done

        	if i.id==10:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 210, 15)		# done 	// ........

        	if i.id==11:
        		self.affiche_pieces_bleu(canvas, i, 0, 5)			# done	

        	if i.id==12:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 75, 460)		# done

        	if i.id==13:
        		self.affiche_pieces_bleu(canvas, i, 180, 415)		# done	


        	if i.id==14:
        		self.affiche_pieces_bleu(canvas, i, 17, 350)		# done


        	if i.id==15:
        		self.affiche_pieces_bleu(canvas, i, 180, 120)		# done


        	if i.id==16:
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 10, 480)		# done

        	if i.id==17:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 160, 575)		# done

        	if i.id==18:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 130, 630)		# done

        		

        	elif i.id==19:
        		i.rotation()
        		i.rotation()
        		self.affiche_pieces_bleu(canvas, i, 20, 640)


        	elif i.id==20:
        		self.affiche_pieces_bleu(canvas, i, 80, 745)


        #canvas.create_rectangle(0, 50, 120, 300, outline="#fb0", fill="#fb0")

        				#canvas.create_line(i.id +20, i.id +25, 200, 25)
        	

		
#        canvas.create_line(15, 25, 200, 25)
#        canvas.create_line(300, 35, 300, 200, dash=(7, 4))
#        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)


        canvas.pack(fill=BOTH, expand=1)



def main():

    root = Tk()
    root.title('BLOCUS')
    root.geometry("1440x860")

    ex = Example(root)
    root.mainloop(0)


if __name__ == '__main__':
    main()
