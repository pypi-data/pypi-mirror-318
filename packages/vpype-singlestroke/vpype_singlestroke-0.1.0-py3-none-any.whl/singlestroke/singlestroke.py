import vpype as vp
import vpype_cli
import click
import numpy as np
from typing import List, Union
import logging

@click.command()
@vpype_cli.global_processor
def singlestroke(
    document: vp.Document
) -> vp.Document:
    """Convert closed paths to open paths by tracing unique vector points.
    
    For each closed path, creates an open path that includes each unique vector point
    exactly once. For a closed path with 2n points (where points[0] = points[2n-1]),
    the result will be n points forming an open path.
    """
    result = document.empty_copy()
    logger = logging.getLogger()
    
    for layer_id, layer in document.layers.items():
        new_layer = vp.LineCollection()
        path_count = 0
        
        for line in layer:
            if len(line) < 2:
                new_layer.append(line)
                continue
                
            points = np.array(line)
            
            # Check if path is closed
            if np.all(points[0] == points[-1]):
                path_count += 1
                logger.info(f"Closed path #{path_count} - Original points: {len(points)}")
                
                # For a closed path, we expect pairs of points
                # Total points should be even (last point equals first)
                n = (len(points) - 1) // 2  # Number of unique points we expect
                
                # Track seen points and their order
                seen_points = {}  # Use dict to maintain first occurrence
                
                # First pass: record first occurrence of each point
                for i, point in enumerate(points[:-1]):  # Skip last point (same as first)
                    point_tuple = (float(point.real), float(point.imag))
                    if point_tuple not in seen_points:
                        seen_points[point_tuple] = i
                
                logger.info(f"  Found {len(seen_points)} unique points")
                
                # Create new path using first occurrence of each point
                # but only up to expected number of points
                indices = sorted(list(seen_points.values()))[:n]
                if len(indices) >= 2:
                    new_points = points[indices]
                    logger.info(f"  Created new path with {len(new_points)} points")
                    new_layer.append(new_points)
            else:
                # Keep non-closed paths as they are
                new_layer.append(points)
        
        if not new_layer.is_empty():
            result.add(new_layer, layer_id)
    
    return result

singlestroke.help_group = "Plugins" 