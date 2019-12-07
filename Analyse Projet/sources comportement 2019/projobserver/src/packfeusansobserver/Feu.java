package packfeusansobserver;

public class Feu 
{
	
	private Couleur couleur;
	public enum Couleur { VERT, ORANGE, ROUGE;	}	
	
	
	public Feu() 
	{	couleur = Couleur.VERT;					}	
	
	
	public void changeCouleur() 
	{
		switch (couleur) 
		{
			case VERT : couleur = Couleur.ORANGE; break;
			case ORANGE : couleur = Couleur.ROUGE; break;
			case ROUGE : couleur = Couleur.VERT; break;
		}
	}
	
	
    public Couleur getCouleur() 
	{	return couleur;		}
}

