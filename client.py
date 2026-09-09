import math

class RiemannianSphereOptimizer:
    """Optimization on the unit sphere S^2 manifold."""
    def step(self, point: list[float], euclidean_grad: list[float], lr: float = 0.1) -> dict:
        # 1. Tangent projection: v = grad - <grad, x> * x
        dot = sum(p * g for p, g in zip(point, euclidean_grad))
        tangent = [g - dot * p for p, g in zip(point, euclidean_grad)]

        # 2. Retraction: R_x(-lr * v) = normalize(x - lr * v)
        unnorm = [p - lr * t for p, t in zip(point, tangent)]
        norm = math.sqrt(sum(x ** 2 for x in unnorm))
        new_point = [round(x / norm, 5) for x in unnorm]

        return {
            "initial_point": point,
            "tangent_gradient": [round(t, 5) for t in tangent],
            "retracted_point": new_point,
            "on_manifold": abs(math.sqrt(sum(x**2 for x in new_point)) - 1.0) < 1e-4
        }
