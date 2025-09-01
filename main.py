from manim import *
class Block:
    def __init__(self,text:str):
        self.square=Square(color=BLUE,fill_opacity=0.7,side_length=1)
        self.text=Text(text,font="SimSun")
    def move_to(self,point:list[int|float]):
        self.square.move_to(point)
        self.text.move_to(point)
    def change_text(self,text:str|int|float):
        return Transform(self.text,Text(str(text),font="SimSun").move_to(self.square))
    def change_color(self,color:ManimColor):
        return self.square.animate.set_color(color)
class Road:
    def __init__(self):
        self.road:list[Block|None]=[Block(str(i+1) if i!=8 else "") for i in range(8)]+[None]
        self.vacancy=8
    def draw(self,square:Square):
        i=0
        for block in self.road:
            if block!=None:
                block.move_to([i%3-1,1-i//3,0])
                i+=1
        return FadeIn(square),*[FadeIn(self.road[i].square) for i in range(8)],*[FadeIn(self.road[i].text if self.road[i].text!=None else Text(" "))  for i in range(8)]

class Main(Scene):
    def construct(self):
        self.text=Text("在上一期视频中",font="SimSun").to_edge(DOWN)
        self.play(FadeIn(self.text))
        self.wait(1)
        square=Square(side_length=3,fill_opacity=0.5,color=BLUE)
        road=Road()
        self.play(road.draw(square))
        caption(self,"我展示了一个判断华容道是否可解的程序",4)
        caption(self,"这期视频的目的是解释程序的原理",4)
        caption(self,"上图是一个华容道",2)
        caption(self,"我们可以移动方块",1)
        replacement(self,7,road)
        replacement(self,4,road)
        replacement(self,7,road)
        replacement(self,8,road)
        caption(self,"我们可以发现",1)
        replacement(self,7,road)
        replacement(self,8,road)
        caption(self,"每一次移动都等价于空白位置与相邻方块的置换",5)
        caption(self,"由此，不难得知",2)
        self.play(*[road.road[i].change_color(RED) for i in range(1,8,2)])
        caption(self,"当空白处在红色部分时一定经过了奇数次的置换",4)
        caption(self,"当空白处在蓝色部分时一定经过了偶数次的置换",4)
        caption(self,"我说的置换不仅指空白块与相邻块的置换",4)
        caption(self,"还包括所有一个块和另一个块的置换",3)
        caption(self,"可以自己想一想这是为什么",2)
        self.play(*[road.road[i].change_color(BLUE) for i in range(1,8,2)])
        self.play(*[road.road[i].change_text(str(2-i)) for i in range(1,3)])
        caption(self,"来看此场景",1)
        self.play(*[road.road[i].change_color(RED) for i in range(1,8,2)])
        caption(self,"此时空白处位于蓝色位置",3)
        caption(self,"说明此时一定经过了偶数次置换",3)
        caption(self,"但显然，这个场景中只经过了奇数次置换",4)
        caption(self,"也就是数字1与数字2的置换",3)
        caption(self,"所以，这显然不可以还原",3)
        self.play(*[road.road[i].change_color(RED) for i in range(1,8,2)])
        self.play(*[road.road[i].change_text(str(i)) for i in range(1,3)])
        caption(self,"但是所有空白位置与置换次数相对应的情况",4)
        caption(self,"就一定都可以还原吗",2)
        self.play(*[road.road[i].change_text((2,1,None,4)[i]) for i in (0,1,3)])
        caption(self,"来看此场景",1)
        caption(self,"在该场景中，1、2、4这三个块的位置",4)
        caption(self,"进行了一次逆时针的置换",2)
        caption(self,"让我们来复原它",1)
        replacement(self,5,road)
        replacement(self,4,road)
        replacement(self,1,road)
        replacement(self,1,road)
        replacement(self,0,road)
        replacement(self,3,road)
        replacement(self,4,road)
        caption(self,"停",1)
        caption(self,"刚才的三步在不影响其他块的情况下",3)
        caption(self,"就完成了对1、2、4这三个块的置换",4)
        self.play(*[road.road[i].change_color(RED) for i in (0,1,3)])
        caption(self,"这启发我们，是否可以将我们要置换的三个块",4)
        caption(self,"放入红色块中，同时将空白块放入中心块中",4)
        caption(self,"然后在不影响其他的块时",2)
        caption(self,"对这三个块做顺或逆时针的置换",3)
        caption(self,"再按照怎么放进来的，怎样放回去",3)
        caption(self,"即可实现在不影响其他块的情况下",3)
        caption(self,"对任意三个实心块做置换操作",3)
        self.play(*[road.road[i].change_color(BLUE) for i in (0,1,3)])
        replacement(self,5,road)
        replacement(self,8,road)
        caption(self,"不难得知，只要能对任意三个实心块做置换",3)
        caption(self,"就能实现任意奇数个实心块做置换",4)
        caption(self,"接下来说的可能有点难懂",3)
        caption(self,"配上例子可能更容易理解",2)
        self.play(*[road.road[i].change_text((2,1,None,5,4)) for i in (0,1,3,4)])
        caption(self,"来看这个情况",1)
        caption(self,"这符合我们之前所说的，空白位置与置换次数相同",5)
        caption(self,"但它一定有解吗",2)
        caption(self,"用直接复原的方法很麻烦",2)
        caption(self,"这时就可以用把任意奇数个块置换的方法了",4)
        caption(self,"来试验一下",1)
        self.play(*[road.road[i].change_text((1,5,None,2)[i]) for i in (0,1,3)])
        self.play(*[road.road[i].change_text(str(i)) for i in (1,3,4)])
        caption(self,"我们可以发现两个互不相干的置换可以解决",4)
        caption(self,"而又不难得知",1)
        caption(self,"任何偶数个块置换都可以化成两个块置换",4)
        caption(self,"结合上面的结论，可以得出",2)
        caption(self,"如果空白块落在右下角，当情况有解时",4)
        caption(self,"则一定可以用三个实心块置换复原",3)
        caption(self,"反之不可以",1)
        caption(self,"而能用三个块置换复原等价于置换数为偶数",4)
        self.play(*[road.road[i].change_color(RED) for i in range(1,8,2)])
        caption(self,"当空心块落在蓝色块上时",3)
        caption(self,"要变换成空心块在右下角需要偶数次置换",4)
        caption(self,"当落在红色块上时，则要奇数次",3)
        self.play(*[road.road[i].change_color(BLUE) for i in range(1,8,2)])
        caption(self,"所以，只有空心块位置与置换次数对应时",4)
        caption(self,"华容道才有解",1)
        self.play(*[FadeOut(road.road[i].square if road.road[i]!=None else Text("")) for i in range(9)],
                  *[FadeOut(road.road[i].text if road.road[i]!=None else Text("")) for i in range(9)],
                  FadeOut(square),
                  Transform(self.text,Text("视频制作不易，求给个点赞")))

def replacement(api:Main,a:int,road:Road):
    i=road.vacancy
    if a==i+1 or a==i-1 or a==i+3 or a==i-3:
        b=road.road[a].square.get_center
        api.play(road.road[a].text.animate.move_to([i%3-1,1-i//3,0]),road.road[a].square.animate.move_to([i%3-1,1-i//3,0]))
        road.road[a],road.road[road.vacancy]=road.road[road.vacancy],road.road[a]
        road.vacancy=a

def caption(api:Main,text:str,time:int|float):
    api.play(Transform(api.text,Text(text,font="SimSun").to_edge(DOWN)))
    api.wait(time)
