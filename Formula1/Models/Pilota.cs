using System.ComponentModel.DataAnnotations;
public class Pilota
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Scuderia { get; set; }
    public int AnnoCampionato { get; set; }
    public string NomeCampionato { get; set; }
    public int PosizionePodio { get; set; }
}