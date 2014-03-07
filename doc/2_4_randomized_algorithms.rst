2.4 乱択アルゴリズムとアドバーザリモデル
=========================================================

* 前節でOPTと最悪の入力sでは、競合比によるページングアルゴリズムの評価が困難であるという説明

  * では正当な評価が可能な方法の提示をしてくれるのかと思いきや... **違う**

* 今節は **「乱択による評価対象のアルゴリズムの(最悪入力列に対する)強化」** の話

  * なので2.3のページングアルゴリズムはやはり評価が困難なまま、に見える

* そもそも乱択アルゴリズムとは

  * 全体を把握するための乱択アルゴリズム

    * 全体を捕らえたいが、全体があまりにも大きくて把握が困難な場合にランダムサンプリングを行う

  * 最悪を回避するための乱択アルゴリズム

    * Quick Sortのピボットの乱択

  * 多数の証拠を得るための乱択アルゴリズム

    * 確率的素数判定。出力は「確実に合成数である」または「おそらく素数である（判定失敗確率付）になる。

* 今回のは2番めの「入力に依存して最悪の事態に陥るのを回避する」目的での乱択アルゴリズム採用（たぶん）。

  * それにより2.3であったような最悪の入力と最強のアルゴリズムを相手にした際の競合比に関して、 :math:`k_{\rm deterministic} > k_{\rm randomized}` という関係が導かれる。それを以下に関して色々証明。

    * レンタルスキー問題 (2.4.1)
    * ページング (2.4.2)
    * リストアクセス (2.4.4)

* 本節で学ぶべきは、入力が全く予想できないような場合には、乱択要素をアルゴリズムに入れることで、最悪の事態 (計算量などコスト) となることを避けられる

アドバーザリ (Adversary)
---------------------------------------------------------

.. list-table:: Adversary
   :widths: 1 4 4
   :header-rows: 1
   :stub-columns: 1

   * - \
     - Adaptive
     - Oblivious
   * - ON
     - Adaptive Adversary + On-line 
     - Oblivious Adversary + On-line
   * - OFF
     - Adaptive Adversary + Off-line
     - Oblivious Adversary + Off-line



* Adversary: 敵、競争相手

* Adaptive Adversary: 実行時の挙動を見てそれに対抗する策を講じる

  * [AOFF] Adaptive offline model: Adaptive Adversary + 最適offline algorithm. すべてのdataが揃ってから対策を講じる. 最強.
  * [AON] Adaptive online model: Adaptive Adversary + online algorithm. onlineでdataを参照しつつ対策を講じる. まあまあ.

* [OBL] Oblivious Adversary: 実行プログラムを見て、それに対抗する策を事前に作成する. 最弱.

[定理 2.10]
   任意のオンライン問題に対し、モデル :math:`M` に対する乱択アルゴリズム ALGの競合比の期待値を :math:`\bar{R}_M ({\rm ALG})` とすると、
.. math::
   \bar{R}_{\rm OBL}({\rm ALG}) \leq \bar{R}_{\rm AON}({\rm ALG}) \leq \bar{R}_{\rm AOFF}({\rm ALG})
