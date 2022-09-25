<template>
	<view>
		<view class="tittle center bold">
			学生免费流量申请表
		</view>

		<view class="time center">
			<view class="bold">
				<!-- 加粗 -->
				申请时间：{{date}}
			</view>
		</view>

		<view class="excel-tittle center bold">
			申请人基本信息
		</view>

		<view>
			<form @submit="formSubmit">
				<!-- 提交键 -->
				<view class="card">
					<view class="interval bold">
						认证账号:{{id}}
					</view>
				</view>

				<view class="card">
					<view class="interval bold">
						姓名：{{userName}}
					</view>
				</view>

				<view class="card">
					<view class="interval bold">
						性别：{{gender}}
					</view>
				</view>

				<view class="card">
					<view class="interval bold">
						学院：{{department}}
					</view>
				</view>

				<view class="card">
					<view class="interval bold">
						专业：
					</view>
					<input v-model="Project" name="专业" placeholder="请输入专业" />
				</view>

				<view class="card">
					<view class="interval bold">
						宿舍地址：
					</view>
					<input v-model="dorm" name="宿舍地址" placeholder="请输入宿舍地址" />
				</view>

				<view class="card">
					<view class="interval bold">
						联系电话：
					</view>
					<input v-model="phonenumber" name="联系电话" placeholder="请输入联系电话" />
				</view>

				<view class="card">
					<view class="interval bold">
						辅导员姓名：
					</view>
					<input v-model="teacherName" name="辅导员姓名" placeholder="请输入辅导员姓名" />
				</view>

				<view class="card">
					<view class="interval bold">
						辅导员联系电话：
					</view>
					<input v-model="teacherPhonenumber" name="辅导员联系电话" placeholder="请输入辅导员联系电话" />
				</view>


				<view class="card">
					<view class="interval bold">
						申请额度：
					</view>
					<radio-group v-model="howMuch" name='额度' class="radio-card">
						<label>
							<radio value="0" v-model="howMuch"/><text class = "radio">10G</text>
						</label>
						<label>
							<radio value="1" v-model="howMuch"/><text class = "radio">30G</text>
						</label>
						<label>
							<radio value="2" v-model="howMuch""/><text class = "radio">50G</text>
						</label>
					</radio-group>
				</view>

				<view class="card">
					<view class="interval bold">
						申请原因简述
					</view>
					<input v-model="reason" name="申请原因简述" placeholder="请简述申请原因" />
				</view>


				<view class="card">
					<view class="interval bold">
						申请相关附件
					</view>
					<uni-section title="选择相关附件">
						<uni-file-picker file-mediatype="all"  @progress="progress"
							@success="success" @fail="fail" @select="select" /><!-- 各种文件类型 -->
						</uni-file-picker>
					</uni-section>
				</view>

				<view>
					<button form-type="submit">提交</button>
				</view>
			</form>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				id:"",
				userName: "",
				gender: "",
				department: "",
				Project: "",
				dorm: "",
				phonenumber: "",
				teacherName: "",
				teacherPhonenumber: "",
				howMuch: "",
				reason: "",
				date: new Date().getFullYear() + "-" + (new Date().getMonth()+1) + "-" + new Date().getDate()
			}
		},
	
	
		methods: {
			upload() {
				this.$refs.files.upload()
			},
			select(e) { // 获取上传状态
				console.log('选择文件：', e)
			},
			progress(e) { // 获取上传进度
				console.log('上传进度：', e)
			},
			success(e) { // 上传成功
				console.log('上传成功')
			},
			fail(e) { // 上传失败
				console.log('上传失败：', e)
			},
			formSubmit: function(e) { //点击确认按钮后
				console.log(this.Project)
	
				var formdata = e.detail.value //字典
				var content = ""
				for (var i in formdata) {
					content += i + ": " + formdata[i] //显示表单数据
				}
				uni.showModal({
					title: '表单数据内容：',
					content: content,
					success:(res) => {
						if (res.confirm) {
							console.log('用户点击确定');
							console.log(this.Project)
							//if(Project.length != 0 && dorm.length != 0 && phonenumber.length != 0 && teacherName.length != 0 && teacherPhonenumber.length != 0 && howMuch.length != 0 && reason.length != 0){
								let that = this
								uni.request({
									url: 'http://127.0.0.1:8000/tableSubmit/current',
									method: 'GET',
									data: {
										Project: this.Project,
										dorm: this.dorm,
										phonenumber: this.phonenumber,
										teacherName: this.teacherName,
										teacherPhonenumber: this.teacherPhonenumber,
										howMuch: this.howMuch,
										reason: this.reason,
									},
									success: (res) => {
										
										if (res.data.status_code == 100) {
											uni.showToast({
												title: '提交成功ヾ(≧▽≦*)o'
											})
										} else {
											console.log(res.data)
											uni.showToast({
												title: '提交失败Σ(°ロ°)',
												comment: '请稍后重试...',
											
											})
										}
									}
								})
							
							//else{
								//uni.showToast({
									//title: '信息都没填完还想交？'
								//})
							//}
						} else if (res.cancel) {
							console.log('用户点击取消');
						}
					},
					showCancel: true //是否有取消按钮
				});
			},
			getData(){
				let that = this
				uni.request({
					url:'http://127.0.0.1:8000/tableSubmit/fixedInfo',
					method:'GET',
					
					success:(res) => {
						
						this.id=res.data.id,
						this.userName=res.data.name,
						this.gender=res.data.gender,
						this.department=res.data.department
					}
				})
			}
		},
		onLoad(res) {
			this.getData();
			let that = this;
			setInterval(function(){
				// uni.setStorageSync('cardnumber',that.cardnumber)
				uni.setStorageSync('name',that.name)
				uni.setStorageSync('gender',that.gender)
				uni.setStorageSync('Project',that.Project)
				uni.setStorageSync('dorm',that.dorm)
				uni.setStorageSync('phonenumber',that.phonenumber)
				uni.setStorageSync('teacherName',that.teacherName)
				uni.setStorageSync('teacherPhonenumber',that.teacherPhonenumber)
				uni.setStorageSync('howMuch',that.howMuch)
				uni.setStorageSync('reason',that.reason)
				uni.setStorageSync('id',that.id)
				uni.setStorageSync('department',that.department)
			},2000)
			
		},
		onShow(res){
		this.getData();
		this.name = uni.getStorageSync('name')
		this.gender = uni.getStorageSync('gender')
		this.Project = uni.getStorageSync('Project')
		this.dorm = uni.getStorageSync('dorm')
		this.phonenumber = uni.getStorageSync('phonenumber')
		this.teacherName = uni.getStorageSync('teacherName')
		this.teacherPhonenumber = uni.getStorageSync('teacherPhonenumber')
		this.howMuch = uni.getStorageSync('howMuch')
		this.reason = uni.getStorageSync('reason')
		this.id = uni.getStorageSync('id')
		this.department = uni.getStorageSync('department')
		}
	}
</script>

<style>
	.center {
		display: flex;
		justify-content: center;
		align-items: center;
	},

	.bold {
		font-weight: 700;
	},

	.tittle {
		font-size: larger;
		margin: 8rpx;
	},

	.time {
		font-size: samll;
	},

	.excel-tittle {
		font-size: large;
		margin: 40rpx;
	},

	.interval {
		/* 项目标题和内容间距 */
		margin-bottom: 10rpx;
	},

	.card {
		/* 项目 */
		padding: 20rpx;
		margin-left: 50rpx;
		margin-right: 50rpx;
		margin-bottom: 35rpx;
		background-color: rgba(242, 242, 242, 0.5);
		border-radius: 20rpx;
	},
	.radio-card{
		display: flex;
		flex-wrap: nowrap;
	},
	.radio{
		margin-right: 20rpx;
	}
</style>
