package packjeuavecstate;

public abstract class EtatJeuVideo
{	
	private JeuVideo jeu;
	
	public EtatJeuVideo(JeuVideo jeu) 
	{	this.jeu = jeu;		}
	
	public abstract void ajouterUtilisateur(Utilisateur user);
	public abstract void retirerUtilisateur(Utilisateur user);
	public abstract void efface();
	public abstract EtatJeuVideo etatSuivant();

	public JeuVideo getJeu() 
	{	return jeu;			}
}
