using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Formula1.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CampionatiController : ControllerBase
    {
        private readonly DbCampionati _context;

        public CampionatiController(DbCampionati context)
        {
            _context = context;
        }

        // GET: api/Campionati
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Pilota>>> GetCampionati()
        {
            return await _context.Campionati.ToListAsync();
        }

        // GET: api/Campionati/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Pilota>> GetPilota(int id)
        {
            var pilota = await _context.Campionati.FindAsync(id);

            if (pilota == null)
            {
                return NotFound();
            }

            return pilota;
        }

        // PUT: api/Campionati/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutPilota(int id, Pilota pilota)
        {
            if (id != pilota.Id)
            {
                return BadRequest();
            }

            _context.Entry(pilota).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!PilotaExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Campionati
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Pilota>> PostPilota(Pilota pilota)
        {
            _context.Campionati.Add(pilota);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetPilota", new { id = pilota.Id }, pilota);
        }

        // DELETE: api/Campionati/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeletePilota(int id)
        {
            var pilota = await _context.Campionati.FindAsync(id);
            if (pilota == null)
            {
                return NotFound();
            }

            _context.Campionati.Remove(pilota);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool PilotaExists(int id)
        {
            return _context.Campionati.Any(e => e.Id == id);
        }
    }
}
