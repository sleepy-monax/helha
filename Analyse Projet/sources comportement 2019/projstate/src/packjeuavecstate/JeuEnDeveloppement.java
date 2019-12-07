package packjeuavecstate;

public class JeuEnDeveloppement extends EtatJeuVideo 
{
	public JeuEnDeveloppement(JeuVideo jeu)
	{	super(jeu);				}

	@Override 
	public void ajouterUtilisateur(Utilisateur user){}		

	@Override 
	public void retirerUtilisateur(Utilisateur user){}	

	@Override 
	public void efface() 
	{	this.getJeu().getUtilisateurs().clear();	}

	@Override 
	public EtatJeuVideo etatSuivant()
	{	return new JeuBeta(this.getJeu());			}
}
