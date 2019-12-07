package packjeusansstate;
import java.util.ArrayList;		
								
public class JeuVideo 
{

	private String nom;
	private ArrayList<Utilisateur> utilisateurs;
	
	private EtatJeuVideo etatJeu;
	public enum EtatJeuVideo { DEVELOPPEMENT, BETA, DEFINITIF };	
	
	public JeuVideo(String nom) 
	{							 
		this.nom = nom;			
		utilisateurs = new ArrayList<Utilisateur>();
		etatJeu = EtatJeuVideo.DEVELOPPEMENT;
		
	}
	
	public void ajouterUtilisateur(Utilisateur user) 
	{
		if (etatJeu == EtatJeuVideo.DEFINITIF || etatJeu == EtatJeuVideo.BETA) 
		{	utilisateurs.add(user);		}
	}
	
	public void retirerUtilisateur(Utilisateur user) 
	{
		if (etatJeu == EtatJeuVideo.DEFINITIF)
		{	 utilisateurs.remove(user);	}
	}
	
	public void efface() 
	{
		if (etatJeu == EtatJeuVideo.DEVELOPPEMENT || etatJeu == EtatJeuVideo.BETA) 
		{	utilisateurs.clear();		}
	}
	
	public void etatSuivant() 
	{
		switch (etatJeu) 
		{
			case DEVELOPPEMENT : etatJeu = EtatJeuVideo.BETA; break;
			case BETA : etatJeu = EtatJeuVideo.DEFINITIF; break;
			case DEFINITIF : break;
		}
	}
	
	public String toString() 
	{
		String tmp = "Nom du jeu : " + nom + " : " + etatJeu;
		for (Utilisateur user : utilisateurs) 
		{	tmp += "\n" + user;	}		
										
		return tmp;
	}
}
