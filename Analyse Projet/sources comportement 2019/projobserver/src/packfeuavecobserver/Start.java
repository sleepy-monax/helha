package packfeuavecobserver;
import packfeuavecobserver.Feu.Couleur;

public class Start 
{
	public static void main(String[] args) 
	{
		 
		Feu unFeu = new Feu();
		unFeu.changeCouleur();					
		
		Voiture voit1 = new Voiture("ECR 949");
		voit1.demarrer();

		Voiture voit2 = new Voiture("CHU 690");
		voit2.demarrer();

		
		System.out.println();
		if (unFeu.getCouleur() != Couleur.VERT)	 
		{
			voit1.sarreter();
			voit2.sarreter();
			unFeu.ajoute(voit1);				 
			unFeu.ajoute(voit2);
		}


		System.out.println("\n-----------------------------------------------------------");
		System.out.println("DESIGN PATTERN OBSERVER (une liste de voitures a été créée)");
		System.out.println("-----------------------------------------------------------");
		System.out.print("Liste des observers : ");
		unFeu.affichageListeObservers();
		System.out.println();
		
		unFeu.changeCouleur();					
	    
		System.out.println();
		unFeu.changeCouleur();
		 
		System.out.print("\nListe des observers après changement de couleur du feu : ");
		unFeu.affichageListeObservers();
		
	}
}