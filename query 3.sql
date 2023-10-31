-- Crear un procedimiento almacenado para obtener las 5 películas con mayor duración en minutos
CREATE OR REPLACE FUNCTION GetTop5LongestMoviesByYear (IN year_param INT)
RETURNS TABLE (
    title VARCHAR(255),
    duration INT
) AS $$
BEGIN
    -- Crear una tabla temporal para almacenar los resultados
    CREATE TEMPORARY TABLE IF NOT EXISTS TempTopMovies (
        title VARCHAR(255),
        duration INT
    );

    -- Insertar las películas con mayor duración en la tabla temporal
    INSERT INTO TempTopMovies (title, duration)
    SELECT s.title, s.duration
    FROM Shows s
    WHERE EXTRACT(YEAR FROM s.date_added) = year_param
    ORDER BY s.duration DESC
    LIMIT 5;

    -- Devolver los resultados utilizando RETURN QUERY
    RETURN QUERY
    SELECT * FROM TempTopMovies;

    -- Eliminar la tabla temporal
    DROP TABLE IF EXISTS TempTopMovies;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM GetTop5LongestMoviesByYear(2019);
