package packjeuavecstate;

public class JeuDefinitif extends EtatJeuVideo 
{
	public JeuDefinitif(JeuVideo jeu) 
	{	super(jeu);						}

	@Override 
	public void ajouterUtilisateur(Utilisateur user) 
	{	this.getJeu().getUtilisateurs().add(user);		}

	@Override 
	public void retirerUtilisateur(Utilisateur user) 
	{	this.getJeu().getUtilisateurs().remove(user);	}

	@Override 
	public void efface() {}

	@Override
	public EtatJeuVideo etatSuivant() 
	{	return this;	}
}
