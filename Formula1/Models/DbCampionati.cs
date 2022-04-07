using Microsoft.EntityFrameworkCore;
public class DbCampionati : DbContext
{
    public DbSet<Pilota> Campionati { get; set; }
	public DbCampionati(DbContextOptions<DbCampionati> options)
		: base(options)
	{
	}

}