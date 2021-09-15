import inspect
from typing import get_type_hints, Any


class AnnotationMismatchError(TypeError):
	def __init__(self, argName:str, annotationsType:Any):
		self.message = f"Mismatch annotation and argument types.\nThe type of argument ({argName}) is {annotationsType}."

	def __str__(self):
		return f"AnnotationMismatchError: {self.message}"


def chk_args(func):
	spec = inspect.getfullargspec(func)
	annotations = spec.annotations

	def _chk_args(argName:str, val:Any):
		if argName in annotations:
			if annotations[argName] == Any:
				return val
			elif issubclass(type(val), annotations[argName]):
				#サブクラスのとき
				return val
			elif type(val) != annotations[argName]:
				raise AnnotationMismatchError(argName, annotations[argName])
			else:
				return val
		else:
			#未指定
			return val

	def wrapper(*args:list, **kwargs:dict):
		i = 0
		_args = list(args)
		for argName, val in zip(spec.args, args):
			_args[i] = _chk_args(argName, val)
			i += 1
		for argName, val in zip(list(kwargs.keys()),list(kwargs.values())):
			kwargs[key] = _chk_args(argName, val)
		return func(*_args, **kwargs)
	return wrapper


