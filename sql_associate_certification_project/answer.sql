-- Task 1 
SELECT 
    id,
    COALESCE(location, 'Unknown') AS location,
    CASE 
      WHEN total_rooms BETWEEN 1 AND 400 THEN total_rooms
      ELSE 100 
    END AS total_rooms,
  
    CASE
      WHEN staff_count IS NOT NULL THEN staff_count
      ELSE total_rooms * 1.5 
    END AS staff_count,
  
    CASE
      WHEN opening_date = '-' THEN '2023' WHEN opening_date BETWEEN '2000' AND '2023' THEN opening_date
      ELSE '2023' 
    END AS opening_date,
  
    CASE
      WHEN target_guests IS NULL THEN 'Leisure' WHEN LOWER(target_guests) LIKE 'b%' THEN 'Business'
      ELSE target_guests 
    END AS target_guests
FROM 
    branch;

-- Task 2
WITH average_time_service AS (
  SELECT 
    service_id,
    branch_id,
    ROUND(AVG(time_taken)::numeric, 2) AS avg_time_taken,
    ROUND(MAX(time_taken)::numeric, 2) AS max_time_taken
  FROM 
    request
  GROUP BY 
    service_id, branch_id
)

SELECT * FROM average_time_service;

-- Task 3
WITH target_hotels AS (
  SELECT 
    s.description,
    b.id AS branch_id,
    b.location,
    r.id AS request_id,
    r.rating
  FROM 
    request r
    JOIN service s ON r.service_id = s.id
    JOIN branch b ON r.branch_id = b.id
  WHERE 
    s.description IN ('Meal', 'Laundry')
    AND b.location IN ('EMEA', 'LATAM')
)

SELECT * FROM target_hotels;

-- Task 4
WITH average_rating AS (
  SELECT 
    service_id,
    branch_id,
    ROUND(AVG(rating)::numeric, 2) AS avg_rating
  FROM 
    request
  GROUP BY 
    service_id, branch_id
  HAVING 
    AVG(rating) < 4.5
)

SELECT * FROM average_rating;