package packjeuavecstate;

import java.util.ArrayList;	

public class JeuVideo 
{	
	private String nom;
	private ArrayList<Utilisateur> utilisateurs;
	private EtatJeuVideo etatJeu;
	
	public JeuVideo(String nom) 
	{
		this.nom = nom;
		utilisateurs = new ArrayList<Utilisateur>();
		etatJeu = new JeuEnDeveloppement(this);	
												
	}
	
	public void ajouterUtilisateur(Utilisateur user) 
	{	etatJeu.ajouterUtilisateur(user);		}
	
	public void retirerUtilisateur(Utilisateur user) 
	{	etatJeu.retirerUtilisateur(user);		}
	
	public void efface() 
	{	etatJeu.efface();						}
	
	public void etatSuivant() 
	{	etatJeu = etatJeu.etatSuivant();		}
	
	
	public String toString() 
	{
		String tmp = "Nom du jeu : "+nom;
		for (Utilisateur user : utilisateurs) 
		{	tmp += "\n" + user;		}
		return tmp;
	}

	public ArrayList<Utilisateur> getUtilisateurs() 
	{	return utilisateurs;					}
}