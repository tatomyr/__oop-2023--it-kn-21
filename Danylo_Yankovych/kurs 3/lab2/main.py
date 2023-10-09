// Класи з сумісними інтерфейсами: КруглийОтвір та
// КруглийКілочок.
class RoundHole is
    constructor RoundHole(radius) { ... }

    method getRadius() is
        // Повернути радіус отвору.

    method fits(peg: RoundPeg) is
        return this.getRadius() >= peg.getRadius()

class RoundPeg is
    constructor RoundPeg(radius) { ... }

    method getRadius() is
        // Повернути радіус круглого кілочка.


// Застарілий несумісний клас: КвадратнийКілочок.
class SquarePeg is
    constructor SquarePeg(width) { ... }

    method getWidth() is
        // Повернути ширину квадратного кілочка.


// Адаптер дозволяє використовувати квадратні кілочки й круглі
// отвори разом.
class SquarePegAdapter extends RoundPeg is
    private field peg: SquarePeg

    constructor SquarePegAdapter(peg: SquarePeg) is
        this.peg = peg

    method getRadius() is
        // Обчислити половину діагоналі квадратного кілочка за
        // теоремою Піфагора.
        return peg.getWidth() * Math.sqrt(2) / 2


// Десь у клієнтському програмному коді.
hole = new RoundHole(5)
rpeg = new RoundPeg(5)
hole.fits(rpeg) // TRUE

small_sqpeg = new SquarePeg(5)
large_sqpeg = new SquarePeg(10)
hole.fits(small_sqpeg) // Помилка компіляції, несумісні типи.

small_sqpeg_adapter = new SquarePegAdapter(small_sqpeg)
large_sqpeg_adapter = new SquarePegAdapter(large_sqpeg)
hole.fits(small_sqpeg_adapter) // TRUE
hole.fits(large_sqpeg_adapter) // FALSE