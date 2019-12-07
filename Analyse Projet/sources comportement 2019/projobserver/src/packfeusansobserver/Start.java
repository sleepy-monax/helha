package packfeusansobserver;
import packfeusansobserver.Feu.Couleur;

public class Start 
{

	public static void main(String[] args) 
	{
	  
		Feu unFeu = new Feu();						
		unFeu.changeCouleur();
		
		Voiture voit1 = new Voiture();	 
		System.out.print("V1 : "); 		
		voit1.demarrer();				
		
		Voiture voit2 = new Voiture();	
		System.out.print("V2 : ");		 
		voit2.demarrer();   			 
		
		System.out.println();
		if (unFeu.getCouleur() != Couleur.VERT)
		{
			System.out.print("V1 : ");				
			voit1.sarreter();					 
			voit1.setFeuDevantV(unFeu);			
			System.out.print("V2 : ");
			voit2.sarreter();					
			voit2.setFeuDevantV(unFeu);			
		}
		
		System.out.println();
		System.out.print("V1 : ");		
		voit1.demarrer();				
		System.out.print("V2 : ");		
		voit2.demarrer();				
		
		unFeu.changeCouleur();						
		
		System.out.println();
		System.out.print("V1 : ");				
		voit1.demarrer();
		System.out.print("V2 : ");
		voit2.demarrer();
		
		System.out.println();
		unFeu.changeCouleur();					
		System.out.print("V1 : ");
		voit1.demarrer();
		System.out.print("V2 : ");
		voit2.demarrer();
	}
}
