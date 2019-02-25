class hello:
  def hi(self,x):
    self._x=x
  def print1(self):
    print(x)
def main():
  t=hello()
  t.hi(1000)
  t.print1()
if __name__=="__main__":main()
