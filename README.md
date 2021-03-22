# MinecraftBE-AutoFishingTool
  自动钓鱼，解放生产力（大误）<br>
  在一次去下界以后弄丢了好友弄来的附魔弓，而游戏内自动钓鱼装置被更新失效了，故做此蠢事弥补损失。虽然弓找回来了，但是这个蠢蠢的小工具给我钓来好几箱附魔书。
  
# Something has went wrong
It's been a long time I haven't use these tool until one day my friend and I created a new world and enjoyed ourselves on an island until we came to a position in which was hard to push anything forward. It suddenly occured to me that I had an auto fishing tool which can brought us enchanted books. As I was fishing, I noticed that Mojang changed the color of the splashing water, resulting in a low efficiency in auto-fishing. Maybe there waas nothing changed and it was only my illusion. If the color does change, I reckon that someone in Mojang noticed this kind of tools and took it for a damage on the fragile balance of enchantment in Minecraft so they adopt measures to stop it. Although the old saying goes where there's a will, there's a way, However, I think I may not fix this tool anymore in order to show respect to the game maker. New splasing water is not as clear as those in old editions, fixing this tool may resulting in more hazy effect which shall harm the gaming experience. They developed this very splendid game, I shall not harm make it bad by my scripts. Coding is to make the world a better place but not destory one. However, I still hope Mojang can bring us new items and features that can free us from dull work and gain more happiness in this wounderful game. It's too difficult, labour intensive and time-consuming to in enchantment. I often find it's hard to make poisons and enchant tools. Sometimes I just can't find the mobs for blaze mods or never find enough Lapis Lazuli for enchantment. What's more, the game is lack efficient travelling vehicle. The world is big but travelling though which is desperating. 

## 写在前面
  我得承认这个东西需要严苛的环境，独占的操作，还容易出意外导致钓鱼终止。看在能在某种程度上解放不得无时无刻不盯着浮标的痛苦钓鱼现状的份上，也算有些价值。<br>
![又不是不能用](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1595955470235&di=022176a7e5d283642446ecca672a93cb&imgtype=0&src=http%3A%2F%2Fbbs-static.smartisan.cn%2Fdata%2Fattachment%2Fforum%2F201811%2F23%2F185450dmavxh9r5ebbn1ez.jpg)<br>
  支持的环境：我只试过 Win10 (不过本来就只有win10有微软商店版本的基岩版吧）

## 自动钓鱼原理
  通过鼠标附近25个红色通道监测点的平均颜色作为判断，在鱼竿水花溅起的时候自动右键（笑）~~*没错就是这么蠢的思路*~~<br>
  用`pyautogui`进行鼠标操作，`ctypes`提取颜色。<br>
  监测阵为以鼠标为中心，横竖轴上0px，±50px，±100px共25个检测点。<br>
  每次放下鱼竿3秒后，进行第一次取样并记作基准平均色a。而后不断取颜色做平均值b并与基准平均色a对比，当颜色差的绝对值大于`sensitivity`时右键鱼竿升起。<br>
  为了实现自动钓鱼做了一些辅助操作，如天暗了以后要修正。当连续20次检测没有超过`sensitivity`时，将此刻的平均颜色b赋值给基准平均色a。<br>
  其中有蜜汁bug会导致返回的颜色全部为255，连续5次检测都为255时自动收勾并重启。<br>
  在小工具启动的时候，会自动点击鼠标左键以获得焦点并继续游戏。而后自动右键抛勾。在约100次循环（约半分钟）没有鱼上钩的时候，判断可能没有抛下鱼钩，此时进行一次额外的右键操作以抛下鱼钩。<br>
  钓鱼将自动在200次后停止。不过没错的话你也撑不到自动完成200次。<br>
  一般在20次左右就会因为返回颜色全部255而重启。所以要默认这个工具会无限运行下去。<br>
**因为30秒重新抛勾机制，电脑不会在钓鱼中断后触发自动休眠。在例如命令行挡住了按键，鼠标被碰飞走以后无法重新获得游戏焦点的时候，只能人工干预来回到钓鱼状态，小工具既不会纠正，也不会休眠。**（后续兴许会加上自动休眠，原理也不难，现在懒）<br>
  如果你的电脑不会出255bug，那么将会在`fishingCounter`次后结束。改成无限就去把`for fishTimeCount in range(fishingCounter):`那一行改成`While True:`

## 使用方法
- 首先你要安装好带pip的Python 3。[Python.org](https://www.python.org)
- 安装一下外部库……懒人神器→ 自动钓鱼简化环境配置器.cmd
- 不要改变小程序的名字，除非想你自己改自启动代码
- 打开你的MinecraftBE缩放到合适的位置
- 选择安全的水边，走近低头，使得丢下浮标后浮标在鼠标附近100像素之内，而不因为随机浮动出发收勾。最好测试一次抛勾-来鱼-自动钓起循环，方为合适位置。
- 按动`Esc`，测试在Minecraft失去焦点后，鼠标是否在"继续游戏"按钮上。如果不是，请移动上去。务必把命令行窗口放远一点，点击命令行窗口后检查命令行是否挡住“继续游戏按钮”。最好多留点空间。
- 回到钓鱼状态，若能完成钓鱼循环就不用理它了。
